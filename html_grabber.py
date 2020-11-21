import requests
from bs4 import BeautifulSoup


def grab(url: str) -> str:
    return requests.get(url).text


# Returns advert_ids for each page
def get_ids(url: str) -> list:
    soup = BeautifulSoup(grab(url), "html.parser")

    types = ["", " red", " blue", " yellow"]

    pre_result = list()

    for t in types:
        ads = soup.find_all("div", class_=f"row list-item{t} a-elem")
        ids = [ad["data-id"] for ad in ads]
        pre_result.append(ids)

    return [j for i in pre_result for j in i]

# Returns the last page to grab from
def get_max_page(url: str) -> int:
    soup = BeautifulSoup(grab(url), "html.parser")
    return int(soup.find(class_="pager").find('ul').find_all('li')[-1].text)
