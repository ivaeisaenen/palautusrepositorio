import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url)
        players_json = response.json()

        # print("JSON-muotoinen vastaus:")
        # print(players_json)

        self.players_list = []

        for player_dict in players_json:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            self.players_list.append(player)