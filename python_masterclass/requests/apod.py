import streamlit as st
import requests

api_key = "NXcDpZcfAaZhC7k8t9hT2P4SI4hwpEnJGk2lDVg8"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date=2025-09-24"

response = requests.get(url)
content = response.json()
image_url = content["url"]
explanation = content['explanation']
title = content['title']
print(content)


st.title("APOD NASA Practice")
st.image(image_url)
st.header(title)
st.text(content["date"])
st.text(explanation)
# st.write(content)
