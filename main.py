import requests
from bs4 import BeautifulSoup

host = "https://avtoelon.uz/"
category = "avto/"

response = requests.get(host + category)

html = response.text

soup = BeautifulSoup(html, "html.parser")

types = ["", " red", " blue", " yellow"]

for t in types:
    ads = soup.find_all("div", class_=f"row list-item{t} a-elem")
    ids = [ad["data-id"] for ad in ads]
    print(ids)
