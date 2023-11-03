import json
import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

fests_all_list = []
for i in range(0, 192, 24):
    url = (f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=3%20Nov%202023&to_date'
           f'=&genre%5B%5D=pop&maxprice=500&o={i}&bannertitle=August')
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'folder_with_festivals_html/index_{i}.html', 'w') as file:
        file.write(html_response)

    with open(f'folder_with_festivals_html/index_{i}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='card-details-link')

    for item in cards:
        fest_url = 'https://www.skiddle.com' + item.get('href')
        fests_all_list.append(fest_url)


info_festivals = []
for url in fests_all_list:
    print(url)
    req = requests.get(url=url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        info_festivals.append(
            {
                'fest_name': soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-1jkv0o6').text,
                'fest_date': soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text,
                'fest_location': soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol")[1].text
            }
        )
    except Exception as ex:
        print(ex)
        print('Error')


with open(f'folder_with_json_festvals/festivals.json', 'w', encoding='utf-8') as file:
    json.dump(info_festivals, file, ensure_ascii=False, indent=4)


