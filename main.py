import requests
from bs4 import BeautifulSoup

from html_grabber import get_ids, get_max_page


def save_data_to_csv(id_list: list):
    import pandas as pd
    df = pd.DataFrame(id_list, columns=["colummn"])
    df.to_csv('list.csv', index=False)


host = "https://avtoelon.uz/"
category = "avto/"

page_num = 1
ids_count = 0
while page_num <= get_max_page(host + category):
    ids = get_ids(host + category + "?page=" + str(page_num))
    ids_count += len(ids)
    print("page =", page_num, "ids found =", len(ids))
    save_data_to_csv(id_list=ids)
    page_num += 1
    if page_num == 3:
        break

print()
print(ids_count)
