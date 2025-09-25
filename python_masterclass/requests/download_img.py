import requests

url = "https://www.emp-online.com/dw/image/v2/BBQV_PRD/on/demandware.static/-/Sites-master-emp/default/dw4b2c5fe7/images/2/3/5/9/235997.jpg?sfrm=png"

r = requests.get(url)

with open("slipknot.jpg", "wb") as file:
    file.write(r.content)

