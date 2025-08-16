# import glob

# myfiles = glob.glob("text_folder/*.txt")

# print(myfiles)

import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))