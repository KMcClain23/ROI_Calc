

# Income - Rental Income $2,000, Laundry $0, storage $0, misc $0
    # Total Monthly Income = $2,000

# Expenses -
    # Tax $150 (Not sure how to find? go to your tax assessor at county), Insurance $100, Utilities $0 - #Electric, Water, Sewer, Garbage, Gas
    # HOA $0, Lawn $0, vacancy $100, repairs $100, CapEx $200 (New Roof, Water Heater, etc...), Property Management $200, mortgage $860
    #     Total Monthly Expenses - $1,610

# Cash Flow = Income - Expenses
    # Total Monthly Cashflow - $390/month

#Cash on Cash ROI (What percentage of your money are you making?
    # Down Payment $40,000, closing costs $3,000, rehab budget $$7,000, misc $0
        # Total Investment - $50,000

    # Annual Cashflow = Monthly Cash Flow $390 * 12 == $4,680
        # Annual Cashflow $4,680 / Total Investment $50,000 = Cash on Cash ROI 9.36%

class Roi_calc():
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.monthly_cash_flow = 0
        self.cash_on_cash_roi = 0
        self.annual_cash_flow = 0

    def income(self):
        rental_income_response = float(input("What is your monthly rental income? $"))
        laundry_income_response = float(input("What is your laundry income? $"))
        storage_income_response = float(input("What is your storage income? $"))
        misc_income_response = float(input("What, if any, is your misc income? $"))

    def expense(self):
        mortgage_expense_response = float(input("How much is your mortgage? $"))
        tax_expense_response = float(input("How much do you pay towards taxes? $"))
        insurance_expense_response = float(input("How much do you pay for insurance? $"))
        # print("How about your utilities like Electric, water, etc...?")
        electric_utility_expense_response = float(input("How much do you pay for electricity? $"))
        water_utility_expense_response = float(input("How much do you pay for water? $"))
        sewer_utility_expense_response = float(input("How much do you pay for sewer? $"))
        garbage_utility_expense_response = float(input("How much do you pay for garbage/recycling? $"))
        gas_utility_expense_response = float(input("How much do you pay for gas? $"))
        hoa_expense_response = float(input("How much do you pay for HOA? $"))
        lawn_expense_response = float(input("How much do you pay for lawn care? $"))
        vacancy_expense_response = float(input("How much are you setting aside for vacancy? $"))
        repairs_expense_response = float(input("How much are you setting aside for repairs? $"))
        capex_expense_response = float(input("How much are you setting aside for capital expense (New Roof, Water Heater, etc...)? $"))
        property_management_expense_response = float(input("How much do you pay for property management? $"))
        misc_expense_response = float(input("Any miscellaneous monthly expense amount $"))


class Main():
    # def cash_flow(self):

