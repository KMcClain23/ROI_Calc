class RentalProperty:
    def __init__(self, rental_income, expenses, total_investment):
        self.rental_income = rental_income
        self.expenses = expenses
        self.total_investment = total_investment

    def calculate_cash_flow(self):
        return self.rental_income - self.expenses

    def calculate_cash_on_cash_roi(self):
        annual_cash_flow = self.calculate_cash_flow() * 12
        return (annual_cash_flow / self.total_investment) * 100


def main():
    rental_income = 2000
    expenses = {
        "tax": 150,
        "insurance": 100,
        "hoa": 0,
        "lawn_snow": 0,
        "vacancy": 100,
        "repairs": 100,
        "capex": 200,
        "property_management": 200,
        "mortgage": 860
    }
    total_expenses = sum(expenses.values())
    total_investment = 50000  # Down payment + closing costs + rehab budget

    property = RentalProperty(rental_income, total_expenses, total_investment)
    cash_flow = property.calculate_cash_flow()
    cash_on_cash_roi = property.calculate_cash_on_cash_roi()

    print(f"Total Monthly Cashflow: ${cash_flow:.2f}")
    print(f"Cash on Cash ROI: {cash_on_cash_roi:.2f}%")


if __name__ == "__main__":
main()
