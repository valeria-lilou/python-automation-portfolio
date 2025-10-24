# This program will create a data file for the properties of North American wildflowers found 
# in the western region.

from pathlib import Path

# Wildflower Data
WILDFLOWER_DATA = [
    {
        'Flower': 'Common Sunflower', 
        'Color': 'Yellow', 
        'Habitat': ['plains', 'foothills', 'roadsides', 'field edge'],
        'Page': 378
     },
     {
        'Flower': 'Blue Columbine', 
        'Color': 'Blue', 
        'Habitat': ['mountains', 'aspen groves'],
        'Page': 706
         
     },
     {
        'Flower': 'English Daisy', 
        'Color': 'White', 
        'Habitat': ['lawns', 'fields', 'roadsides'],
        'Page': 359
     }
]
# Create Path:
FILE_PATH = Path('test_data') / 'wildflower_data.txt'

# Create Folder:
FILE_PATH.parent.mkdir()

# Open File:
with open(FILE_PATH, 'w') as file:
    
    file.write(WILDFLOWER_DATA)