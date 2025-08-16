password = input("Enter password: ")
result = {
    "length" : False,
    "digit" : False,
    "upper" : False
}

if len(password) >= 8:
    result["length"] = True

for char in password:
    if char.isdigit():
        result["digit"] = True

    if char.isupper():
        result["up_case"] = True
print(result)

if all(result.values()):
    print("Password is strong")
else:
    print("Password is weak")