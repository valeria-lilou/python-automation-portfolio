# This program will take your favorite morning caffeinated drink order.
# Let me know your comfort sip!

import pyinputplus as pyip

#Prompt for user's drink order
print('\nMorning! What can I get started for you?\n')

#Get user's order: drink, dairy preferences, flavor 
drink = pyip.inputMenu(['Latte', 'Cappuccino', 'Mocha'],
                       prompt='')

#Prompt if dairy is okay
print('\nIs dairy okay?\n')

dairy_alt = pyip.inputMenu(['Oat', 'Almond', 'Coconut', 'Dairy Ok'],
                       prompt='')

# Prompt if the user would like to add flavor
add_flavor = pyip.inputYesNo('\nWould you like to add a flavor? (yes/no)\n')
# If yes, prompt flavors
if add_flavor == 'yes':
    flavor = pyip.inputMenu(['Vanilla', 'Hazelnut', 'Caramel', 'White Chocolate'],
                       prompt='')
   
    print(f'\nYour {flavor} {drink} will be right out!\n')
# If no, repeat complete order to user
else:
    print(f'\nSounds good! Your {drink} will be right out.\n')
