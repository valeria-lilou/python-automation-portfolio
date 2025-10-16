# This program will take your favorite morning caffeinated drink order.
# Let me know your comfort sip!
# By using PyInputPlus to get the user's 

import pyinputplus as pyip

#Prompt for user's drink order
print('\nMorning! What can I get started for you?\n')

#Get user's order: drink, dairy preferences, flavor 
drink = pyip.inputMenu(['Latte', 'Cappuccino', 'Espresso', 'Mocha', 'Cafe au Lait'],
                       prompt='')

#Prompt if dairy is okay
print('\nIs dairy okay?\n')

#Yes/No input validation

#If yes prompt flavor
#If no prompt dairy alternatives

dairy_alt = pyip.inputMenu(['Oat', 'Almond', 'Coconut', 'Dairy Okay'],
                       prompt='')

# Prompt if the user would like to add flavor
print('\nWould you like to add a flavor?\n')
# If yes, prompt flavors
add_flavor = pyip.inputMenu(['Vanilla', 'Hazelnut', 'Caramel', 'White Chocolate'],
                       prompt='')
# If no, repeat complete order to user

print(f'\nYour {add_flavor} {drink} will be right out!')