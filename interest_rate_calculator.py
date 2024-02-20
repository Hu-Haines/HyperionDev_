''' This is a interest calculator that calculates interest on investments and bonds'''


import math

# Error checking functions
# checking it's not an integer and asks unser for new input if not so
def check_not_int(user_input):
    while True:
        try:
            user_input = int(user_input)
            user_input = input('[error1]Enter a valid input:\n      ')
        except:
            user_input=user_input.lower().strip().strip(".").strip(",")
            return user_input

# checks whether user input is either a or b and asks user for new input if not so
def check_is_a_and_b(user_input):
    while True:
        try:
            user_input = user_input.lower().strip().strip(".").strip(",")
            
            if user_input == 'a':
                return user_input
            elif user_input == 'b':
                return user_input
            else:
                user_input = input('[error2]Enter a valid input:\n      ')

        except:
            user_input = input('[error3]Enter a valid input:\n      ')

# checks whether user input is a float, stripping away all unnessesary inputs and asks user for new input of not
def check_is_float(user_input):
    while True:
        try:
            user_input.lower().strip().strip(".").strip(",") # General stripping
            user_input.strip("£").strip("pounds").strip("pound") # If user input is money value related 
            user_input.strip("%").strip("percentage").strip("percent") # If user input is percent related
            user_input = float(user_input)
            return user_input
        except:
            user_input = input('[error4]Please enter in a numeric form:\n           ')



# repeats the calculator unless the user says no at the end of the running through the calculator
while True:
    # asking user for investment or bond 
    variable = input("""
        [a] Investment - to calculate the amount of interest you'll earn on your investment 
        [b] Bond       - to calculatethe amount you'll have to pay on a home loan

        Enter either 'a' or 'b' from the menu above to proceed:
        """ ).lower()
    variable = check_not_int(variable)
    variable = check_is_a_and_b(variable)


    # if the user chooses investment
    if variable == "a":
        deposit = input("How much are you depositing? ")
        deposit = check_is_float(deposit)
        interest_rate = input("What is the interest rate? ")
        interest_rate = check_is_float(interest_rate)
        years = input("How many years do you plan on investing? ")
        years = check_is_float(years)
        interest = input('''Would you like simple or compound interest?
                            [a] Simple
                            [b] Compund\n''')
        interest = check_is_a_and_b(interest)
        
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
        house = input("What is the present value of the house? ")
        house = check_is_float(house)
        interest_rate = input("What is the interest rate? ")
        interest_rate = check_is_float(interest_rate)
        months = input("Number of months do you plan to take to repay the bond: ")
        months = check_is_float(months)
        monthly_interest = (interest_rate/100)/12
        repayment = (monthly_interest * house) / (1 - (1 + monthly_interest)**(-months))
        print(f"You will have to repay £{repayment} per month!")
    
    to_continue = input('would you like to use the calculator again? [a] yes    [b] no\n')
    to_continue = check_not_int(to_continue)
    to_continue = check_is_a_and_b(to_continue)
    if to_continue == 'b':
        break
    


# end message 
print('Good Bye.')