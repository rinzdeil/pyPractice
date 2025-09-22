import requests
import smtplib
import ssl

topic = "Coffee"
api_key = "pub_24ef48753f724b2fbb54c334321e7d2f"
url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={topic}&language=en"

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    password = "akkq dmgl ljny gcjb"
    email = "dalesumande@gmail.com"
    receiver = email

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver , message)

response = requests.get(url)
content = response.json()

lines = ""

for article in content['results']:
    title = article['title']
    description = article['description']
    link = article['link']

    lines = lines + f"\n{title}\n{description}\nLink: {link}" + "\n\n"

default_message = f"""\
Subject: Latest News about {topic}

{lines}
"""
send_email(default_message.encode("utf-8"))
print(default_message)

