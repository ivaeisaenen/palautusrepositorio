from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    # Some test printing for task 2
    print()
    matcher2_1 = And(Not(HasAtLeast(1, "goals")), PlaysIn("NYR"))
    for player in stats.matches(matcher2_1):
        print(player)

    print()
    matcher2_2 = And(HasFewerThan(1, "goals"),PlaysIn("NYR"))
    for player in stats.matches(matcher2_2):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))




if __name__ == "__main__":
    main()
