''' This program calculates the cost of a holiday with assisted guidance on choices '''

# User-introduction 
print('''
                             Welcome to Space Travel Holidays cost guider! 
      
              It's tough to make time and space for a holiday in this intergalactic space
              In the years of 100,200s, you were able to save enough money for a holiday! 
          This is suppose to be impossible according to the intergalactic-government-system(IGS)
                    Since this is a rarity, we will help you make all your savings count!
''')
input("Press enter to continue...")


# Part One: Collecting all the variables
# Destination: this gives all the available destinations and stores the number correlated with the desination in the destination variable
destination = input('''
                Lets have a look at all of the galatic points you can enjoy your holiday:
                      
    All traveling destinations are seasonal due to hindering space rocks and allignments, we apologise in
    advance if what you are looking for isn't in our list. However, enjoy this seasons destinations before 
    it's too late!
                      
            [1] - Earth: monther of our species humans [£250,000 per flight]
                    Come here for history. Have you ever wondered where we came from? 
                    This is OUR birth sphere, the singular dot before expansion. 
                    This place is rich history and whole with knowlege, 
                    and can make you feel grounded once more.

            [2] - The Edge: most outer edge of our known galacticspace [£500,000 per flight]
                    Do you want to wonder? Look into the outer most rim
                    where nothing is touched or known to us humans.
                    Have a relaxing time at the edge of nowhere!

            [3] - The Archives: the biggest library of human made data within galacticspace [£300,000 per flight]
                    Do you want to know where is the actual location where all our data resorts to?
                    Welcome to THE ARCHIVES and enjoy the magnificent view of the machines at work


    Please enter the number ^^
                      ''').replace('[', '').replace(']','')
# This turns and checks the destination is an integer and whether it's one of our options, and gives feedback on the choices they have made. 
# Also stores the name of the destination for future use
while True:
    try:
        destination = int(destination)
        if destination == 1:
            destination_name = 'Earth'
            print(f'{destination_name} is a fabulous place to understand your origins again, Great Choice!')
            break
        elif destination == 2:
            destination_name = 'The Edge'
            print(f'{destination_name} is for the ones who wonders, Great Choice!')
            break
        elif destination == 3:
            destination_name = 'The Archives'
            print(f'{destination_name} is for the ones who cant stop learning, Great Choice!')
            break
        else:
            print('You didnt enter one of our options, please try again ^^')
            destination = input(': ').replace('[', '').replace(']','').strip()  
    except:
            print('please enter the number correlated with the option, lets try again^^\n')
            destination = input(': ').replace('[', '').replace(']','').strip()


# Duration: asks for how many nights they want to stay, then checks and stores it as an integer
duration = (input(f'''
                     How many nights would you like to stay at {destination_name}?\n
    '''))
while True:
    try:
        duration = int(duration)
        break
    except:
           print('Please enter in a numeric form!^^')
           duration = input(': ')


# Hotel Options: gives out hotel options correlated with the destination numbers, then stores as a letter
# Within the same loop, for each destination it has it's own error check loop, 
# Which will give correlating responses to their choices, and checks they have entered one of our choices 
if destination == 1:
        Hotel = input(f'''\n Being on {destination_name} where would you like to stay?
                    [a] - a classic Earth hotel [£5,000 per night]
                    [b] - a classic Earth home [£7,000 per night]
                    [c] - on a classic Earth boat [£8,000 per night]
                      \n''').lower().replace('[', '').replace(']','').strip()
        while True:
            if Hotel == 'a':
                hotel_name = 'Marine Bay Sands Hotel in Singapore'
                print('''
                        You will be staying at the ancient Marine Bay Sands Hotel in Singapore! 
                        Looking down on the left overs of what was once a thriving metropolis\n
                      ''')
                break
            elif Hotel == 'b':
                hotel_name = 'The British Cottage'
                print('''           You have selected a classic english cottage!\n ''')
                break
            elif Hotel == 'c':
                hotel_name = 'The Pirate Ship'
                print('''
                                    Earth has been nearly devoured by the ocean 
                                What great choice to be on a pirate ship! Arrr
                        The sea creature are still diverse, take your time and explore <3\n''')
                break
            else:
                    Hotel = input('I dont think you entered one of our options, remember to enter the letter correlated with your choice, try again:\n').lower().replace('[', '').replace(']','').strip()
elif destination == 2:
        Hotel = input(f'''\n Being on {destination_name} where would you like to stay?
                    [d] - the grand circular space resort [£20,000 per night]
                    [e] - your own cozy space craft [£15,000 per night]\n
                    ''').lower().replace('[', '').replace(']','').strip()
        while True:
            if Hotel == 'd':
                hotel_name = 'GOLD Infinite Resorts'
                print('''
                        Feeling luxurious? The Gold Infinite resort gives you everything you ever need!
                            5 star cheffs, infinity pools, gyms, dress-coded parities, personal cinema
                                        social members includes more benefits ofc ;)\n''')
                break
            elif Hotel == 'e':
                hotel_name = 'your own cozy space craft'
                print(''' Why not have an modern space scraft all to yourself!
                                have your own space with you and your loved ones
                                and enjoy the grand view of the nebula \n''')
                break
            else:
                    Hotel = input('I dont think you entered one of our options, remember to enter the letter correlated with your choice, try again:\n').lower().replace('[', '').replace(']','').strip()
elif destination == 3:
        Hotel = input(f'''\n Being on {destination_name} where would you like to stay?
                    [f] - the center orb: [£8,000 per night]
                    [g] - the outer ring: [£10,000 per night]\n
                    ''').lower().replace('[', '').replace(']','').strip()
        while True:
            if Hotel == 'f':
                    hotel_name = 'The Center Orb'
                    print('''   Be right in the center of all the circulating rings
                                Have all knowlege and data circle around you
                                And have hyper access to the archive!\n''')
                    break
            elif Hotel == 'g':
                    hotel_name = 'The Outer Ring'
                    print('''   At the most outer ring of The Archive machine, 
                                you get to enjoy the slow spin circulating 
                                with 360 grand view of the entire archive!\n ''')
                    break
            else:
                    Hotel = input('I dont think you entered one of our options, remember to enter the letter correlated with your choice, try again:\n').lower().replace('[', '').replace(']','').strip()


# Spacecraft: asks would they like a spacecraft, if yes how many days
# An error loop if the user didn't enter either y or n
# And an integer checking loop for number of days want to hire for
craft_decision = input(f"\nWould you like to hire your own space craft?[£3,000 per day] y/n\n").lower().strip()
while True:
    if craft_decision == 'y':
        craft_duration = input(f"\nHow many days would you like to hire the space craft for?") #this needs userinput checker
        while True: # checking user has input an integer
             try:
                  craft_duration = int(craft_duration)
                  break
             except:
                  craft_duration = input("Please enter in a numeric form! \n:")
        print("Alright! This will be sorted for you! ")
        craft_decision = f'You have hired a space craft for {craft_duration} days!'
        break
    elif craft_decision == 'n':
        craft_decision = 'You have not hired a space craft but you wont be missing anything!'
        print("\nThat's alright, there is plenty to view without even leaving your resort!")
        break
    else:
        craft_decision = input("Please enter only the characters 'y' for yes or 'n' for no!\n:").lower().strip()


# Part two: costs 
# Function for hotel cost 
def hotel_costs(duration,Hotel):
    # exchanging hotel to it's correlating cost per night
    if Hotel == 'a':
        per_night = 5000
    elif Hotel == 'b':
        per_night = 7000
    elif Hotel == 'c':
        per_night = 8000
    elif Hotel == 'd':
        per_night = 20000
    elif Hotel == 'e':
        per_night = 15000
    elif Hotel == 'f':
        per_night = 8000
    elif Hotel == 'g':
        per_night = 10000
    hotel_cost = int(duration) * per_night
    return hotel_cost


# Function for plane cost 
def plane_costs(destination):
    if destination == 1:
          plane_cost = 250000 * 2 # 2 is going there and returning back 
    if destination == 2:
          plane_cost = 500000 * 2
    if destination == 3:
          plane_cost = 300000 * 2
    return plane_cost


# Function for space craft cost
def craft_rental(craft_duration):
    craft_cost = int(craft_duration) * 3000
    return craft_cost


# Function for total holiday cost
def holiday_cost(hotel_cost,plane_cost,craft_cost):
    total_cost = hotel_cost + plane_cost + craft_cost
    return(total_cost)



# Part Three: suming up costs and presenting it back to the user
# Calculating the costs according to user's choices
hotel_costs = hotel_costs(duration,Hotel)
plane_costs = plane_costs(destination)
craft_cost = craft_rental(craft_duration)
total_cost = holiday_cost(hotel_costs,plane_costs,craft_cost)


# Final User Ending Page 
print(f''' 
            For your grand trip to {destination_name} it will have an total cost of £{total_cost}!
                            This will be your trip of a life time! 
                Since we won't know when will you be able to get another holiday again!
                Staying at {hotel_name} you will have an amzaing time enjoying yourself <3
                {craft_decision}
                                        --Take care and see you next time
''')