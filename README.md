## Project 1 - Team Gallardo 
## "avtoelon.uz" - parser
#### "Advanced Programming Technologies" course

Hello everyone and welcome to our repository, feel free to leave your questions in comments below

## Web - scraping

This project is about web-parsing site avtoelon.uz which is related to cars and other means of transport's ads. This site is a equivalent to well-known kolesa.kz in Kazakhstan but in
Uzbekistan.

![Web - scraping](https://info.cloudfactory.com/hs-fs/hubfs/website-2016/assets/graphics/use-cases/uc-webscrapping.gif?width=1024&name=uc-webscrapping.gif)

___
### So, what is web - scraping?

Web-scraping is a method used to get
great amounts of data from websites and then data can be used for any kind of data manipulation
and operation on it. Also you can use parsed data against your rivals (in various areas) to get their information and
make forecasts or any kind of analyses. The most convenient things about it are that parsed
material could be stored in one CSV or other files, you can also adjust them by some enquired
parameters, and it is incredibly fast.


_Although web scraping can be done manually, in most cases, you might be better off using an automated tool. After all, these are usually faster and less expensive than scraping data manually._
***

### Briefly about site

If you go to the website, you will see a landing page with many photos of cars for sale. In the header, there are four options of site navigation: cars, spare parts and auto-goods,
repairing and services and commercials. Let’s go to cars -> light ones and set basic parameters to filter. As a result, there are more than thirty thousand advertisements and 1000 of pages, each
page we have only 20 pieces of the ad.


Like every ads-giving site, there are some priority ones with also different colours. The data is nested in tags, so let’s inspect each colour and see the differences in &lt;div&gt; tag classes. Next step we want to inspect the page with Chrome Developer Tool and to find hashtags for every advertisement. 

Here they are:

First one is light orange colour, which has “red” in class:
```
<div class="row list-item red a-elem" data-id="1126238" id="advert-1126238">. 
```
Second one – without colour i.e. white background:
```
<div class="row list-item a-elem" data-id="1169053" id="advert-1169053">. 
```

And next are blue and orange colours:

```
<div class="row list-item yellow a-elem" data-id="1146899" id="advert-1146899">,
```

```
<div class="row list-item blue a-elem" data-id="775213" id="advert-775213">. 
```

***
![Data](https://hackernoon.com/images/r117y3yy2.gif)
### What data do we want to extract?

We choose only the main information about the car. Like the picture of the car and the information like car brand, year of production, mileage, colour and type of transmission.  Little lower we can see the location of the item, the date of the ad and viewing. On the right top corner, there is also a price. 

Here’s how site looks like:

![Avtoelonsite](https://s8.gifyu.com/images/Avtoelonsite.gif)
***
## Sourse code

Project code is divided into some different files such as [main.py](https://github.com/ErkebulanMuhamedkali/avtoelon-parser/blob/main/main.py), [details.py](https://github.com/ErkebulanMuhamedkali/avtoelon-parser/blob/main/details.py) and [html_grabber.py](https://github.com/ErkebulanMuhamedkali/avtoelon-parser/blob/main/html_grabber.py). 
Primary flow runs in main.py. 
To scrap avtoelon.kz we need to iterate over all pages and take ids of each ad on each page. To know when to stop we need to get the last page, and we have get_max_page function for it, which returns the number of the last page. After it we can loop from the first page until last one. 


```
# Iterates through all pages
while page_num <= get_max_page(host + category):
    ids = get_ids(host + category + "?page=" + str(page_num))
    details = []
    for i in ids:
        temp_details = get_details(i, host)
        if temp_details is not None:
            details.append(temp_details)
    ids_count += len(ids)
    print("page =", page_num, "ids found =", len(ids))
    all_data.append(details)
    page_num += 1
    if page_num > 80:
        break
```
While iterating we use the function get_ids to get all adverts’ ids. This function handles all types of ads (they are differentiated by red, blue, yellow colors and without any color) and grabs their ids. 
After getting all ids from the current page, the web simply iterates through them and gets details of each ad id. For it we have get_details function, which gets brand, name, year, price, description and other parameters from the ad's details page. 

```
# Grabs details for each advert
def get_details(ad_id: str, host: str):
    try:
        print("Started getting details from id:", ad_id)
        soup = BeautifulSoup(grab(f"{host}a/show/{ad_id}"), "html.parser")

        brand = soup.find('span', {"itemprop": "brand"}).text.strip()
        name = soup.find('h1', class_='a-title__text').find('span', {"itemprop": "name"}).text.strip()
        year = int(soup.find('span', class_='year').text.strip())
        price = int(''.join(soup.find('span', class_='a-price__text').text.strip().split('\xa0')[:-1]).replace('~', ''))
        pre_result = dict(brand=brand, name=name, year=year, price=price)

        description = soup.find('dl', class_='clearfix dl-horizontal description-params')
        keys = [k.text.strip() for k in description.find_all('dt', class_='value-title')]
        values = [v.text.strip() for v in description.find_all('dd', class_='value clearfix')]
```
To get that page it uses the grab function, which simply returns html content of requested id’s page. While parsing some elements can be not loaded yet, or some other network error may occur, that’s why we have try-except chain which logs everything. 

Each cycle we append grabbed data to all_data list. After the loop ends, we use save_data_to_csv function to convert information in all_data from list to pandas DataFrame and save it in csv ([list.csv](https://github.com/ErkebulanMuhamedkali/avtoelon-parser/blob/main/list.csv)) format.
```
save_data_to_csv([j for i in all_data for j in i])
```
## Analyze

All analysis have been done in Jupyter notebook using following libraries: pandas (dataframe), numpy (mathematical operations and contains array and matrix data structures) and matplotlib.pyplot (for diagrams)

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
In this file you will see detailed analysis with comments [Analyze.ipynb](https://github.com/ErkebulanMuhamedkali/avtoelon-parser/blob/main/Analyze.ipynb). 

## Team members

* **Anefiyayev Nurdaulet** - [qqbnureke](https://github.com/qqbnureke)
* **Dairbekova Madina** - [Dmadina](https://github.com/Dmadina)
* **Alim Sanzhar**  - [alimsanzhar](https://github.com/alimsanzhar)
* **Mukhamedkali Yerkebulan**  - [ErkebulanMuhamedkali](https://github.com/ErkebulanMuhamedkali)



