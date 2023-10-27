import csv
import random
from csv import writer
import json
from time import sleep

import requests
from bs4 import BeautifulSoup

# url = "https://calorizator.ru/product"
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome/ 118.0 "
                  ".0 .0 Safari / 537.36"
}
# req = requests.get(url, headers=headers)
#
# data = req.text
# print(data)
#
# with open('parser_food.html', 'w', encoding='utf-8') as file:
#     file.write(data)

with open('parser_food.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find(class_="node-inner inner").find_all('a')
all_products_category = []

url_cabinet = soup.find(class_="prod37-cabinet")
url_recipes = soup.find(class_="node-content").find('a')
for x in all_products_href:
    if x.text == url_cabinet.text or x.text == '' or x.text == url_recipes.text:
        continue
    else:
        all_products_category.append(x)
print('-' * 100)

all_categories_dict = {}
for x in all_products_category:
    item_text = x.text
    item_href = "https://calorizator.ru/" + x.get('href')
    # print(f"{item_text} {item_href}")
    all_categories_dict[item_text] = item_href

# with open('file_caloriesfoods_parser.json', 'w', encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('file_caloriesfoods_parser.json', encoding='utf-8') as file:
    categories_all = json.load(file)

iteration = int(len(categories_all)) - 1
count = 0
print(f"All iterations: {iteration}")
for category_name, category_href in categories_all.items():
    rep = [",", " ", "-"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"folder_with_html/{count}_{category_name}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open(f"folder_with_html/{count}_{category_name}.html", encoding="utf-8") as file:
        data = file.read()

    soup = BeautifulSoup(data, "lxml")

    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    table_head = soup.find(class_="views-table sticky-enabled cols-6").find_all("a")
    empty = table_head[0].text
    product = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    calories = table_head[5].text

    dates = [empty, product, proteins, fats, carbohydrates, calories]
    with open(f"folder_with_csv_files/{count}_{category_name}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow((empty, product, proteins, fats, carbohydrates, calories))

    product_data = soup.find(class_="views-table sticky-enabled cols-6").find("tbody").find_all("tr")

    product_info = []
    for item in product_data:
        product_tds = item.find_all("td")

        title = product_tds[1].find("a").text
        calories = product_tds[2].text
        proteins = product_tds[3].text
        fats = product_tds[4].text
        carbohydrates = product_tds[5].text

        product_info.append(
            {
                "title": title,
                "calories": calories,
                "proteins": proteins,
                "fats": fats,
                "carbohydrates": carbohydrates
            }
        )

        with open(f"folder_with_csv_files/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    with open(f"folder_with_json/{count}_{category_name}.json", "w", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"Iteration #{count}. {category_name} write...")
    iteration -= 1

    if iteration == 0:
        print('Program final!')
        break
    print(f"Stay: {iteration}")
    sleep(random.randrange(2, 4))
