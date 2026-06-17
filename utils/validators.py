# Validation functions
import re

def is_valid_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def sanitize_expression(expr):
    # Allow numbers, operators, parenthesis, decimal, math functions
    pattern = r'^[0-9+\-*/().%\s^]+$'
    # This is a basic check; full evaluation uses safe_eval with sandboxed dict
    return bool(re.match(pattern, expr.replace('sin', '').replace('cos', '').replace('tan', '').replace('pi', '').replace('log', '').replace('ln', '').replace('sqrt', '')))