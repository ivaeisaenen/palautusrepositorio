from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

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

    # Some test printing for task  2
    print()
    matcher2_1 = And(Not(HasAtLeast(1, "goals")), PlaysIn("NYR"))
    for player in stats.matches(matcher2_1):
        print(player)

    # Sammy Blais          NYR          0  + 4  = 4
    # Libor Hajek          NYR          0  + 1  = 1
    # Tim Gettinger        NYR          0  + 0  = 0
    # Anthony Greco        NYR          0  + 0  = 0
    # Zac Jones            NYR          0  + 2  = 2
    # Keith Kinkaid        NYR          0  + 0  = 0
    # Igor Shesterkin      NYR          0  + 0  = 0
    # Adam Huska           NYR          0  + 0  = 0
    # Alexandar Georgiev   NYR          0  + 0  = 0

    print()
    matcher2_2 = And(HasFewerThan(1, "goals"),PlaysIn("NYR"))
    for player in stats.matches(matcher2_2):
        print(player)

    # Sammy Blais          NYR          0  + 4  = 4
    # Libor Hajek          NYR          0  + 1  = 1
    # Tim Gettinger        NYR          0  + 0  = 0
    # Anthony Greco        NYR          0  + 0  = 0
    # Zac Jones            NYR          0  + 2  = 2
    # Keith Kinkaid        NYR          0  + 0  = 0
    # Igor Shesterkin      NYR          0  + 0  = 0
    # Adam Huska           NYR          0  + 0  = 0
    # Alexandar Georgiev   NYR          0  + 0  = 0

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    # Some test printing for task 3
    print()
    matcher3_1 = Or(HasAtLeast(45, "goals"),HasAtLeast(70, "assists"))
    for player in stats.matches(matcher3_1):
        print(player)

    # Chris Kreider        NYR          52 + 25 = 77
    # Artemi Panarin       NYR          22 + 74 = 96
    # Auston Matthews      TOR          60 + 46 = 106
    # Jonathan Huberdeau   FLA          30 + 85 = 115
    # Alex Ovechkin        WSH          50 + 40 = 90
    # Roman Josi           NSH          23 + 73 = 96
    # Johnny Gaudreau      CGY          40 + 75 = 115
    # Leon Draisaitl       EDM          55 + 55 = 110
    # Connor McDavid       EDM          44 + 79 = 123
    # Kirill Kaprizov      MIN          47 + 61 = 108
    # Kyle Connor          WPG          47 + 46 = 93

    print()
    matcher3_2 = And(HasAtLeast(70, "points"),Or(PlaysIn("NYR"),PlaysIn("FLA"),PlaysIn("BOS")))
    for player in stats.matches(matcher3_2):
        print(player)

    # Chris Kreider        NYR          52 + 25 = 77
    # Mika Zibanejad       NYR          29 + 52 = 81
    # Artemi Panarin       NYR          22 + 74 = 96
    # Adam Fox             NYR          11 + 63 = 74
    # Brad Marchand        BOS          32 + 48 = 80
    # David Pastrnak       BOS          40 + 37 = 77
    # Jonathan Huberdeau   FLA          30 + 85 = 115
    # Aleksander Barkov    FLA          39 + 49 = 88
    # Sam Reinhart         FLA          33 + 49 = 82

if __name__ == "__main__":
    main()
