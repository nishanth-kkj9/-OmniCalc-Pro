# Calculator engine logic
class BasicEngine:
    @staticmethod
    def calculate(expr, angle_mode="degrees"):
        # Delegates to helper safe_eval
        from utils.helpers import safe_eval
        return safe_eval(expr, angle_mode)