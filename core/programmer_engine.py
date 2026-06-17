# Programmer calculator logic
class ProgrammerEngine:
    @staticmethod
    def to_base(value, base="BIN"):
        try:
            val = int(value)
            if base == "BIN": return bin(val)
            elif base == "HEX": return hex(val)
            elif base == "OCT": return oct(val)
            else: return str(val)
        except: return "Invalid"

    @staticmethod
    def bitwise(a, b, op):
        try:
            a_int, b_int = int(a), int(b)
            if op == "AND": return a_int & b_int
            elif op == "OR": return a_int | b_int
            elif op == "XOR": return a_int ^ b_int
            elif op == "NOT": return ~a_int
            else: return 0
        except: return "Error"

    @staticmethod
    def shift(a, n, direction="L"):
        try:
            val = int(a)
            return val << n if direction == "L" else val >> n
        except: return "Error"