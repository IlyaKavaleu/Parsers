import json
from bs4 import BeautifulSoup
import requests


class OTOMOTOParser:
    def __init__(self, url):
        self.url = url

    def scrape_data(self):
        response = requests.get(self.url)

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
                    'name': page_all[ids].text,
                    'all_information': page_all[ids].text,
                    'image': image[ids].text,
                    'city': city[ids].text,
                    'published_date': date_published[ids].text,
                    'price': price[ids].text
                }

                volkswagen_passat_list.append(data)
            return volkswagen_passat_list

    def show_info(self, items):
        for item in items:
            print('Name: ', item['name'])
            print("All information: ", item['all_information'])
            print("Image: ", item['image'])
            print("City: ", item["city"])
            print('Published date: ', item['published_date'])
            print('Price: ', item['price'])
            print('\n')

    def to_json(self, data):
        with open(f"file_otomoto_json/file_volkswagen_passat.json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def main(self):
        data = self.scrape_data()
        self.show_info(data)
        self.to_json(data)


if __name__ == "__main__":
    url = 'https://www.otomoto.pl/osobowe/volkswagen/cc?search%5Bfilter_float_year%3Ato%5D=2011'
    otomoto = OTOMOTOParser(url)
    otomoto.main()
