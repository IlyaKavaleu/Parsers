import json
from bs4 import BeautifulSoup
import requests


class OLXScraper:
    def __init__(self, url):
        self.url = url

    def scrape_data(self):
        response = requests.get(self.url)

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

            return data
        else:
            print("Failed to retrieve the web page")
            return []

    def save_to_json(self, data, filename):
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def show_info(self, data):
        """Print the data for each item"""
        for item in data:
            print("Name:", item["name"])
            print("Price:", item["price"])
            print("City:", item["city"])
            print("Date and Counter:", item["date_and_counter"])
            print("\n")

    def main(self):
        if __name__ == "__main__":
            data = main.scrape_data()
            main.show_info(data)
            main.save_to_json(data, "file_volkswagen_passats_from_olx.json")


if __name__ == "__main__":
    url = "https://www.olx.pl/oferty/q-volkswagen-cc/?search%5Bfilter_float_price:from%5D=10000&search%5Bfilter_float_price:to%5D=35000"
    main = OLXScraper(url)
    main.main()



