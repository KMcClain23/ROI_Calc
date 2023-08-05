

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
        # Cash on Cash ROI 9.36% = Annual Cashflow $4,680 / Total Investment $50,000 

import os
import sys
import time



def loading_animation():
    animation = "|/-\\"
    sys.stdout.write("Loading:")
    for _ in range(8):
        for char in animation:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

# def print_strikethrough(text):
#     strikethrough_text = f"\033[9m{text}\033[0m"
#     return strikethrough_text

# text_to_strike = "Social Security"
# print_strikethrough(text_to_strike)

# strike = print_strikethrough(text_to_strike)

class Roi_calc():
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.monthly_cash_flow = 0
        self.cash_on_cash_roi = 0
        self.annual_cash_flow = 0
    def income(self):
        while True:
            try:
                rental_income_response = float(input("1. What is your monthly rental income? $"))
                laundry_income_response = float(input("2. What is your laundry income? $"))
                storage_income_response = float(input("3. What is your storage income? $"))
                misc_income_response = float(input("4. What, if any, is your misc income? $"))
                total_income = rental_income_response + laundry_income_response + storage_income_response + misc_income_response
                return total_income
            except ValueError:
                clear_output()
                print("Invalid input. You're a human. You should know better. I'm honestly ashamed of you.\n")
    def expense(self):
        while True:
            try:
                mortgage_expense_response = float(input("1. How much is your mortgage? $"))
                tax_expense_response = float(input("2. How much do you pay towards taxes? $"))
                insurance_expense_response = float(input("3. How much do you pay for insurance? $"))
                # print("How about your utilities like Electric, water, etc...?")
                electric_utility_expense_response = float(input("4. How much do you pay for electricity? $"))
                water_utility_expense_response = float(input("5. How much do you pay for water? $"))
                sewer_utility_expense_response = float(input("6. How much do you pay for sewer? $"))
                garbage_utility_expense_response = float(input("7. How much do you pay for garbage/recycling? $"))
                gas_utility_expense_response = float(input("8. How much do you pay for gas? $"))
                hoa_expense_response = float(input("9. How much do you pay for HOA? $"))
                lawn_expense_response = float(input("10. How much do you pay for lawn care? $"))
                vacancy_expense_response = float(input("11. How much are you setting aside for vacancy? $"))
                repairs_expense_response = float(input("12. How much are you setting aside for repairs? $"))
                capex_expense_response = float(input("13. How much are you setting aside for capital expense (New Roof, Water Heater, etc...)? $"))
                property_management_expense_response = float(input("14. How much do you pay for property management? $"))
                misc_expense_response = float(input("15. Any miscellaneous monthly expense amount $"))
                total_expense = mortgage_expense_response + tax_expense_response + insurance_expense_response + electric_utility_expense_response + water_utility_expense_response + sewer_utility_expense_response + garbage_utility_expense_response + gas_utility_expense_response + hoa_expense_response + lawn_expense_response + vacancy_expense_response + repairs_expense_response + capex_expense_response + property_management_expense_response + misc_expense_response
                return total_expense
            except ValueError:
                clear_output()
                print("Invalid input. You're a human. You should know better. I'm honestly ashamed of you.\n")
    
    def cash_on_cash(self, annual_cash_flow, total_investment):
        cash_on_cash = annual_cash_flow / total_investment
        return cash_on_cash
    
    def total_investment(self):
        total_invest_response = float(input("What was your total investment?"))
        return total_invest_response
        
    def cash_flow(self, total_income, total_expense):
        cash_flow = total_income - total_expense
        return cash_flow

    def annual_cash(self, cash_flow):
        annual_cash_flow = cash_flow *12
        return annual_cash_flow
    

def clear_output():
    os.system("cls" if os.name == "nt" else "clear")

class Main:
    clear_output()
    print("Welcome to your ROI calculator.\n\nPutting all our eggs in one basket.")
    loading_animation()
    hello = Roi_calc()
    clear_output()
    print(f"Let's start by gathering your income information.")
    time.sleep(3)
    clear_output()
    print("Please answer these next 4 questions about your income.")
    time.sleep(3)
    clear_output()
    total_income = hello.income()
    print('\n')
    print(f"You've entered a total income of ${total_income:.2f}.")
    response = input("Does that look right? Please choose (y/n)")
    while True:
        if response == 'y':
            clear_output()
            print(f"Next, we will gather your expenses.")
            time.sleep(3)
            clear_output()
            print("Please answer these next 15 questions about your expenses.")
            time.sleep(3)
            clear_output()
            total_expense = hello.expense()
            break
        elif response == 'n':
            clear_output()
            print("Sorry. I'm not perfect...")
            total_income = hello.income()
            print('\n')
            print(f"You've entered a total income of ${total_income:.2f}.")
            response = input("Does that look right? Please choose (y/n)")
            continue
        else:
            clear_output()
            print("Invalid input. Please enter 'y' or 'n'.")
            time.sleep(2)
            clear_output()
            print(f"You've entered a total income of ${total_income:.2f}.")
            response = input("Does that look right? Please choose (y/n)")
            print('\n')
            continue
    clear_output()
    print(f"You've entered a total expense of ${total_expense:.2f}. Does that look right? ")
    cash_flow_value = float(hello.cash_flow(total_income, total_expense))
    print(f"Based on the numbers you have entered, your \|/-\|/-")
    total_investment_value = float(hello.total_investment())
    annual_cash_flow_value = float(hello.annual_cash(cash_flow_value))
    cash_on_cash_roi_value = hello.cash_on_cash(annual_cash_flow_value, total_investment_value)

    print(f"Your Cash ROI is {cash_on_cash_roi_value:.2f}")

Main()


