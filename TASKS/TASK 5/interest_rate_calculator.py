''' This is a interest calculator that calculates interest on investments and bonds'''


import math

# Error checking functions
# checks whether user input is one of the avialable options and asks user for new input if not so
def check_valid_choice(prompt):
    valid_options = ["a", "b"]
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            print("Incorrect choice, please try again...")

# checks whether user input is a float, stripping away all unnessesary inputs and asks user for new input of not
def check_is_float(prompt):
    while True:
        try:
            new_float = float(input(prompt))
            return new_float
        except ValueError:
            print("Incorrect input, please enter a correct numeric value.")




# repeats the calculator unless the user says no at the end of the running through the calculator
while True:
    # asking user for investment or bond 
    variable = input("""
        [a] Investment - to calculate the amount of interest you'll earn on your investment 
        [b] Bond       - to calculatethe amount you'll have to pay on a home loan
        """ ).lower()
    variable = check_valid_choice("Enter either 'a' or 'b' from the menu above to proceed:")

    # if the user chooses investment
    if variable == "a":
        deposit = check_is_float("How much are you depositing?\n       ")
        interest_rate = check_is_float("What is the interest rate?\n      ")
        years = check_is_float("How many years do you plan on investing?\n        ")
        print('Would you like simple or compound interest?')
        interest = check_valid_choice('''                            
                            [a] Simple
                            [b] Compund\n''')
        
    # calculating simple interest
        if interest == "a":
            total = deposit *(1 + (interest_rate/100) * years)
            total = math.ceil(total)
            print(f"You will have £{total} by the end of {years}years with simple interest!")

    # calculating compund interest
        elif interest == "b": 
            interest_rate = interest_rate / 100
            total = deposit * math.pow((1 + interest_rate) , years)
            total = math.ceil(total)
            print(f"You will have £{total} by the end of {years}years with compound interest!")

    # if the user chooses bond
    elif variable == "b":
        house = check_is_float("What is the present value of the house? ")
        interest_rate = check_is_float("What is the interest rate? ")
        months = check_is_float("Number of months do you plan to take to repay the bond: ")
        monthly_interest = (interest_rate/100)/12
        repayment = (monthly_interest * house) / (1 - (1 + monthly_interest)**(-months))
        print(f"You will have to repay £{repayment} per month!")
    
    to_continue = check_valid_choice('would you like to use the calculator again? [a] yes    [b] no\n')

    if to_continue == 'b':
        break
    


# end message 
print('Good Bye.')