# Scientific calculator logic
import math
from utils.helpers import safe_eval

class ScientificEngine:
    @staticmethod
    def calculate(expr, angle_mode="degrees"):
        return safe_eval(expr, angle_mode)

    @staticmethod
    def get_function_list():
        return ["sin", "cos", "tan", "asin", "acos", "atan",
                "log", "ln", "sqrt", "pi", "e", "factorial"]