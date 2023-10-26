import json

from bs4 import BeautifulSoup
import requests

url = 'https://www.otomoto.pl/osobowe/volkswagen/cc?search%5Bfilter_float_year%3Ato%5D=2011'

response = requests.get(url)

if response.status_code == 200:
    src = response.text

    soup = BeautifulSoup(src, 'lxml')

    name = soup.find_all(class_="ev7e6t88 ooa-17thc3y er34gjf0")
    page_all = soup.find_all(class_='ev7e6t89 ooa-1xvnx1e er34gjf0')
    image = list(soup.find_all(class_="ooa-165sslu e1j52kpv10"))
    city = list(soup.find_all(class_="ooa-1o0axny ev7e6t84"))
    date_published = list(soup.find_all(class_="ooa-16w655c ev7e6t83"))
    price = list(soup.find_all(class_="ooa-1wb7q8u ev7e6t814"))

    volkswagen_passat_list = []

    for ids, x in enumerate(name):
        data = {
            'NAME': page_all[ids].text,
            'ALL INFORMATIONS': x.text,
            'IMAGE': image[ids].text,
            'CITY': city[ids].text,
            'PUBLISHED DATE': date_published[ids].text,
            'PRICE': price[ids].text
        }

        volkswagen_passat_list.append(data)

    for entry in volkswagen_passat_list:
        print(entry)

    with open("file_volkswagen_passat.json", "w", encoding='utf-8') as file:
        json.dump(volkswagen_passat_list, file, indent=4, ensure_ascii=False)

else:
    print(f"Ошибка при получении страницы. Статус код: {response.status_code}")




