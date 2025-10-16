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
print('Is dairy okay?')

#Yes/No input validation

#If yes prompt flavor
#If no prompt dairy alternatives

dairy_alt = pyip.inputMenu(['Oat', 'Almond', 'Coconut'],
                       prompt='')

# Prompt if the user would like to add flavor
# If yes, prompt flavors
# If no, repeat complete order to user