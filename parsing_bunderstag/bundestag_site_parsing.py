import json
import requests
from bs4 import BeautifulSoup
import lxml

# persons_url_list = []
# for x in range(0, 740, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true&offset={x}'
#     q = requests.get(url)
#     result = q.content
#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all('a')
#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
#
#
# with open('persons_url.txt', 'w') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')
#
count = 0
data_dict = []
with open('persons_url.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        q = requests.get(line)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_="col-xs-8 col-md-9 bt-biografie-name").find("h3").text
        person_name_consignment = person.strip().split(',')
        person_name = person_name_consignment[0]
        person_consignment = person_name_consignment[1]
        photo = soup.find(class_="col-xs-4 col-md-3 bt-profil-potrait").find(class_="bt-bild-standard pull-left").find('img')

        data = {
            'name': person_name,
            'company': person_consignment,
            'photo': str(photo),
        }
        data_dict.append(data)
        count += 1
        print(f'#Iteration: {count}. {line} is done!')
        with open('folder_bundestag_json/bundestag.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, indent=4)
