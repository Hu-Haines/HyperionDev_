import math

# The sum of all of users attempts except for -1.
total = []

# Introduction to the game.
print("Lets play a game! ")
# Users input is 'number'.
number = (input("Guess a number: ")) 


while True:
    try:
# Identifying that number is an int.
        number = int(number)
# When number is not -1. 
        if number != -1:
            total.append(number) # adding number to the total list
            # tells user to try again and resets 'number'
            number = int(input("What a shame that was incorrect, please try again: "))
            continue
# When the number is -1. 
        else:
            print("Congrats you've gussed the number!")
            break

# When number is not 'int'.
    except:
         print("Please enter a integer in a numerical form instead")
         # tells user to try again and resets 'number'
         number = (input("Guess a number: "))

# Printing out the average of all attempts. 
average = math.fsum(total)/len(total)
print(f'The average of all your attempts before -1 is {average}!')