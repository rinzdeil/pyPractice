contents = [
    "All carrots",
    "All potatoes",
    "All apples"
]

strip_contents = [item.strip("All ") for item in contents]

filenames = ["doc.txt", "report.txt", "presentation.txt"]



# for index, value in enumerate(filenames):
#     print(index, value)
#     file = open(filenames[index], "w")
#     file.write(contents[index])
#     file.close()

for content, fname in zip(strip_contents, filenames):
    file = open(rf"..\files\{fname}", "w")
    file.write(content)
    file.close()
