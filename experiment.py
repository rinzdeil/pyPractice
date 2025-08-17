# import glob

# myfiles = glob.glob("text_folder/*.txt")

# print(myfiles)

# import csv

# filepath = "text_folder/weather.csv"

# with open(filepath, "r") as file:
#     data = list(csv.reader(file))

# city = input("Enter a city: ")

# for row in data[1:]:
#     if row[0] == city:
#         print(row[1])

# import shutil
# shutil.make_archive("output", "zip", "text_folder")

# import webbrowser

# query = input("Enter a search term: ")
# webbrowser.open(f"https://www.google.com/search?q={query}")