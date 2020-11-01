from details import get_details
from html_grabber import get_ids, get_max_page


def save_data_to_csv(adverts: list):
    import pandas as pd
    df = pd.DataFrame(adverts)
    df.to_csv('list.csv', index=False)


host = "https://avtoelon.uz/"
category = "avto/"

all_data = []

page_num = 1
ids_count = 0
while page_num <= get_max_page(host + category):
    ids = get_ids(host + category + "?page=" + str(page_num))
    details = [get_details(i, host) for i in ids]
    ids_count += len(ids)
    print("page =", page_num, "ids found =", len(ids))
    all_data.append(details)
    page_num += 1

save_data_to_csv([j for i in all_data for j in i])

print()
print(ids_count)
