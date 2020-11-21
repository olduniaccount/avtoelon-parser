from bs4 import BeautifulSoup

from html_grabber import grab

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

        parameters = dict(zip(keys, values))
        if 'Пробег' in parameters.keys():
            parameters['Пробег'] = int(''.join(parameters.get('Пробег').split(' ')[:-1]))

        result = {'id': ad_id, **pre_result, **parameters}

        views = soup.find('div', class_='col-sm-4 nb-views').text.strip()
        pub_date = soup.find('div', class_='col-sm-4').text.strip()

        print(f"{ad_id} done")
        return result
    except Exception as e:
        print('*'*100)
        print("Alarm alarm error error in id:", ad_id)
        print("Error:", e)
        print('*'*100)
