


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

def beep_boop_animation():
    animation = "|/-\\"
    sys.stdout.write("beep boop beep bop")
    for _ in range(6):
        for char in animation:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

def animate_typing(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

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
                animate_typing("Invalid input. You are a human. You should know better. I am ashamed of you.\n")
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
                animate_typing("Invalid input. You are a human. You should know better. I am ashamed of you.\n")
    
    def cash_on_cash(self, annual_cash_flow, total_investment):
        cash_on_cash = annual_cash_flow / total_investment
        return cash_on_cash
    
    def total_investment(self):
        total_invest_response = float(input("What was your total investment? $"))
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
    animate_typing("Welcome to Laggy Larry's ROI calculator and foot massage.\n\nPutting all of your eggs in one basket.\n")
    loading_animation()
    hello = Roi_calc()
    clear_output()
    animate_typing(f"Time to get started by gathering your income information.\n")
    beep_boop_animation()
    clear_output()
    animate_typing("Please answer these next 4 questions about your income.\n")
    beep_boop_animation()
    clear_output()
    total_income = hello.income()
    print('\n')
    clear_output()
    print("calculating...you will make me do this a lot.")
    beep_boop_animation()
    clear_output()
    animate_typing(f"\nYou have entered a total income of ${total_income:.2f} per month.\n\n")
    response = input("Does that look right? Please choose (y/n) ")
    while True:
        if response == 'y':
            clear_output()
            animate_typing(f"Great! Next, we will gather your expenses.\n")
            beep_boop_animation()
            clear_output()
            animate_typing("Please answer these next 15 questions about your expenses.\n")
            beep_boop_animation()
            clear_output()
            total_expense = hello.expense()
            break
        elif response == 'n':
            clear_output()
            animate_typing("Sorry. I am not perfect yet...geez\n")
            total_income = hello.income()
            print('\n\n')
            beep_boop_animation()
            clear_output()
            animate_typing(f"\nYou have entered a total income of ${total_income:.2f}.")
            response = input("Does that look right? Please choose (y/n). ")
            continue
        else:
            clear_output()
            animate_typing("Invalid input. Please enter 'y' or 'n'. ")
            time.sleep(2)
            clear_output()
            beep_boop_animation()
            animate_typing(f"\nYou have entered a total income of ${total_income:.2f}.")
            response = input("\nDoes that look right? Please choose (y/n). ")
            print('\n')
            continue
    clear_output()
    beep_boop_animation()
    clear_output()
    animate_typing(f"You have entered a total expense of ${total_expense:.2f}.")
    response = input("\n\nDoes that look right? Please choose (y/n). ")
    while True:
        if response == 'y':
            clear_output()
            animate_typing(f"Next, we will calculate your cash flow.\n")
            beep_boop_animation()
            clear_output()
            break
        elif response == 'n':
            clear_output()
            animate_typing("Sorry. I am only CLOSE to perfect. My bad I guess...")
            total_expense = hello.expense()
            print('\n')
            clear_output()
            animate_typing(f"You have entered a total expense of ${total_expense:.2f}.")
            response = input("Does that look right? Please choose (y/n). ")
            continue
        else:
            clear_output()
            animate_typing("Invalid input. Please enter 'y' or 'n'. ")
            time.sleep(2)
            clear_output()
            animate_typing(f"You have entered a total expense of ${total_expense:.2f}.")
            response = input("Does that look right? Please choose (y/n). ")
            print('\n')
            continue
    cash_flow_value = float(hello.cash_flow(total_income, total_expense))
    if cash_flow_value <= 0:
        animate_typing("Yowzers! I suggest to reach out to another human who works with numbers. You clearly cannot.\n\n")
    beep_boop_animation()
    clear_output()
    animate_typing(f"\nBased on the numbers you have entered, your cashflow is ${cash_flow_value:.2f}\n")
    beep_boop_animation()
    print('\n')
    clear_output()
    total_investment_value = float(hello.total_investment())
    clear_output()
    annual_cash_flow_value = float(hello.annual_cash(cash_flow_value))
    cash_on_cash_roi_value = hello.cash_on_cash(annual_cash_flow_value, total_investment_value)

    animate_typing(f"\nYour Cash ROI is {cash_on_cash_roi_value:.2f}%!\n")
    animate_typing("\nThank you for using Laggy Larry's ROI calculator and foot massage.\n\nFeedback? Find the README on my github page at https://github.com/KMcClain23/ROI_Calc")

Main()