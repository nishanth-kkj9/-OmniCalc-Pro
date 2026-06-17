"""
Safe Expression Evaluator - AST-based, no eval().

Uses sympy's parser with restricted transformations for secure mathematical evaluation.
No code execution possible - only mathematical expressions.
"""
import math
import re
from typing import Any

from sympy import sympify, SympifyError
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    function_exponentiation,
    convert_xor,
)

from utils.logger import get_logger

logger = get_logger()

MAX_EXPR_LENGTH = 500
MAX_RESULT_DIGITS = 50

SAFE_FUNCTIONS = {
    "sin", "cos", "tan", "asin", "acos", "atan",
    "sinh", "cosh", "tanh", "asinh", "acosh", "atanh",
    "log", "ln", "log10", "log2", "sqrt", "cbrt",
    "exp", "expm1", "degrees", "radians",
    "floor", "ceil", "trunc", "round",
    "abs", "factorial", "gamma",
    "pi", "e", "tau", "inf", "nan",
}

SAFE_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": float("inf"),
    "nan": float("nan"),
}

DEGREE_FUNCTIONS = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
}

RADIAN_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "atanh": math.atanh,
    "log": math.log10,
    "ln": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "sqrt": math.sqrt,
    "cbrt": lambda x: x ** (1/3),
    "exp": math.exp,
    "expm1": math.expm1,
    "degrees": math.degrees,
    "radians": math.radians,
    "floor": math.floor,
    "ceil": math.ceil,
    "trunc": math.trunc,
    "round": round,
    "abs": abs,
    "factorial": math.factorial,
    "gamma": math.gamma,
}

TRANSFORMATIONS = (
    standard_transformations
    + (implicit_multiplication_application,)
    + (function_exponentiation,)
    + (convert_xor,)
)

_UNICODE_MAP = {
    "×": "*", "÷": "/", "−": "-", "–": "-",
    "·": "*", "·": "*", "√": "sqrt",
    "π": "pi", "τ": "tau", "∞": "inf",
    "²": "**2", "³": "**3", "ⁿ": "**",
    "±": "+-", "∓": "-+",
    "≤": "<=", "≥": ">=", "≠": "!=",
    "≈": "~", "≡": "==",
}

_NUMBER_RE = re.compile(r"\b(\d+)(\.\d*)?\b")


class SafeEvaluator:
    """Thread-safe mathematical expression evaluator."""

    def __init__(self, angle_mode: str = "degrees", max_length: int = MAX_EXPR_LENGTH):
        self.angle_mode = angle_mode
        self.max_length = max_length
        self._namespace = self._build_namespace()

    def _build_namespace(self) -> dict:
        ns = dict(SAFE_CONSTANTS)
        if self.angle_mode == "degrees":
            ns.update(DEGREE_FUNCTIONS)
            ns.update({k: v for k, v in RADIAN_FUNCTIONS.items() if k not in DEGREE_FUNCTIONS})
        else:
            ns.update(RADIAN_FUNCTIONS)
        return ns

    def set_angle_mode(self, mode: str) -> None:
        if mode in ("degrees", "radians"):
            self.angle_mode = mode
            self._namespace = self._build_namespace()

    def _normalize(self, expr: str) -> str:
        if len(expr) > self.max_length:
            raise ValueError(f"Expression too long (max {self.max_length} chars)")

        expr = expr.strip()
        if not expr:
            raise ValueError("Empty expression")

        for k, v in _UNICODE_MAP.items():
            expr = expr.replace(k, v)

        expr = re.sub(r"(\d)([a-zA-Z\(])", r"\1*\2", expr)
        expr = re.sub(r"(\))(?=[\d\(a-zA-Z])", r"\1*", expr)

        expr = re.sub(r"([+\-*/])\1+", r"\1", expr)
        expr = re.sub(r"\*\*+", "**", expr)

        return expr

    def _validate_ast(self, expr: str) -> None:
        tree = parse_expr(expr, transformations=TRANSFORMATIONS, evaluate=False)

        for node in tree.atoms():
            if node.is_Symbol:
                name = str(node)
                if name not in self._namespace and name not in SAFE_CONSTANTS:
                    raise ValueError(f"Unknown identifier: {name}")

        for func in tree.atoms():
            if func.is_Function:
                fname = func.func.__name__
                if fname not in SAFE_FUNCTIONS:
                    raise ValueError(f"Function not allowed: {fname}")

    def evaluate(self, expr: str) -> float:
        try:
            expr = self._normalize(expr)
            self._validate_ast(expr)

            result = parse_expr(expr, transformations=TRANSFORMATIONS, local_dict=self._namespace, evaluate=True)

            if result.is_number:
                val = float(result)
                if math.isinf(val) or math.isnan(val):
                    raise ValueError("Result is infinite or NaN")
                return val

            raise ValueError("Result is not a number")

        except SympifyError as e:
            logger.warning(f"Parse error: {expr} -> {e}")
            raise ValueError(f"Invalid expression: {e}")
        except (ZeroDivisionError, OverflowError) as e:
            logger.warning(f"Math error: {expr} -> {e}")
            raise ValueError("Math error: division by zero or overflow")
        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Evaluation error: {expr} -> {e}")
            raise ValueError(f"Evaluation failed: {e}")

    def evaluate_safe(self, expr: str) -> float | str:
        try:
            return self.evaluate(expr)
        except ValueError as e:
            return f"Error: {e}"


_default_evaluator = SafeEvaluator()


def safe_eval(expression: str, angle_mode: str = "degrees") -> float | str:
    """Convenience function for backward compatibility."""
    global _default_evaluator
    if _default_evaluator.angle_mode != angle_mode:
        _default_evaluator.set_angle_mode(angle_mode)
    return _default_evaluator.evaluate_safe(expression)