import json
import requests
from bs4 import BeautifulSoup as BS
import lxml


class GAMEParser:
    def __init__(self):
        print(' === Parsing process start === ')

    def scrap(self):
        page = 1
        info = []
        while page < 7:
            res = requests.get(f"https://stopgame.ru/games/action/ps5/best?year_start=2022&p={page}")
            soup = BS(res.text, 'lxml')

            rankings = soup.find_all(class_="_rating-container_2lb1u_1")
            pictures = soup.find_all(class_='_image_2lb1u_13')
            names = soup.find_all('a', class_='_card_2lb1u_1')

            for name, ranking, picture in zip(names, rankings, pictures):
                name = name.get('title')
                ranking = ranking.text.strip()
                picture = picture['src']
                info.append({'name': name, 'ranking': ranking, 'picture': picture})
            page += 1
        return info

    def to_json(self, dates):
        with open('folder_game_with_json/game_json.json', 'w', encoding='utf-8') as file:
            json.dump(dates, file, ensure_ascii=False, indent=4)

    def show(self, dates):
        for data in dates:
            print('Name: ', data['name'])
            print("All information: ", data['ranking'])
            print("Image: ", data['picture'])
            print('\n')


game = GAMEParser()
data = game.scrap()
game.to_json(data)
game.show(data)
