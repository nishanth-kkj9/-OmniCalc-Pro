# Expression parser logic
import sympy as sp

class MathParser:
    @staticmethod
    def parse_expression(expr):
        try:
            expr = expr.replace('^', '**')
            return sp.sympify(expr, evaluate=False)
        except Exception as e:
            raise ValueError(f"Error parsing expression: {e}")

    @staticmethod
    def to_latex(expr):
        return sp.latex(expr)

    @staticmethod
    def solve_for_variable(expr, variable='x'):
        x = sp.Symbol(variable)
        eq = sp.sympify(expr)
        return sp.solve(eq, x)