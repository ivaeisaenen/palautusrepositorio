import requests
from player import Player

def main():
    """{"name":"P.K. Subban",
        "nationality":"CAN",
        "assists":17,
        "goals":5,
        "penalties":82,
        "team":"NJD",
        "games":77}
    """
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url)
    players_json = response.json()

    print("JSON-muotoinen vastaus:")
    # print(players_json)

    players = []

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

        players.append(player)

    print("Oliot:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
