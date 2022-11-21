class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players_ = list(filter(lambda p: p.nationality == nationality, self.reader.players_list))
        players_.sort(key=lambda p: p.points, reverse=True)
        return players_