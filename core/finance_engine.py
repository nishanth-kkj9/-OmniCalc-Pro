# Finance calculator logic
class FinanceEngine:
    @staticmethod
    def emi(principal, annual_rate, months):
        r = annual_rate / 12 / 100
        emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
        total_pay = emi * months
        interest = total_pay - principal
        return round(emi, 2), round(total_pay, 2), round(interest, 2)

    @staticmethod
    def compound_interest(p, r, n, t):
        # p: principal, r: rate %, n: compounds/year, t: years
        amount = p * (1 + (r/100)/n)**(n*t)
        return round(amount, 2), round(amount - p, 2)

    @staticmethod
    def gst(amount, rate, inclusive=True):
        if inclusive:
            original = amount / (1 + rate/100)
            tax = amount - original
            return round(original, 2), round(tax, 2)
        else:
            tax = amount * (rate/100)
            return amount, round(tax, 2), round(amount + tax, 2)

    @staticmethod
    def discount(price, pct):
        saved = price * (pct/100)
        final = price - saved
        return round(saved, 2), round(final, 2)