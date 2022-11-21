import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

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

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players_ = stats.top_scorers_by_nationality("FIN")

    for player in players_:
        print(player)


if __name__ == "__main__":
    main()
