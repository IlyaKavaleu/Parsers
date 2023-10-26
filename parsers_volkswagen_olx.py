import json
from bs4 import BeautifulSoup
import requests

url = "https://www.olx.pl/oferty/q-volkswagen-cc/?search%5Bfilter_float_price:from%5D=10000&search%5Bfilter_float_price:to%5D=35000"
response = requests.get(url)

if response.status_code == 200:
    src = response.text
    soup = BeautifulSoup(src, 'lxml')
    names = soup.find_all(class_="css-16v5mdi er34gjf0")
    prices = soup.find_all(class_="css-10b0gli er34gjf0")
    cities = soup.find_all(class_="css-veheph er34gjf0")
    date_and_counters = soup.find_all(class_="css-efx9z5")

    data = []

    for name, price, city, date_counter in zip(names, prices, cities, date_and_counters):
        name_text = name.text.strip()
        price_text = price.text.strip()
        city_text = city.text.strip()
        date_counter_text = date_counter.text.strip()

        if city_text == '' or date_counter_text == '':
            continue

        item = {
            "name": name_text,
            "price": price_text,
            "city": city_text,
            "date_and_counter": date_counter_text
        }

        data.append(item)

        # Print the data for each item
        print("Name:", name_text)
        print("Price:", price_text)
        print("City:", city_text)
        print("Date and Counter:", date_counter_text)
        print("\n")

    with open("file_volkswagen_passats_from_olx.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
else:
    print("Failed to retrieve the web page")
