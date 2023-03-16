"This program uses a .csv to select random quotes from the csv files"
"Original source https://stackoverflow.com/questions/43476754/using-python-how-do-you-select-a-random-row-of-a-csv-file"

import csv
import random

def breakfast_selection():
    with open('Breakfast_Data.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        print(chosen_row)
breakfast_selection()