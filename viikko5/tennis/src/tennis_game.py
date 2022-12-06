class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.points = 3

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1


    def get_tie_score_string(self):
        if self.player1_score == 0:
            score_string = "Love-All"
        elif self.player1_score == 1:
            score_string = "Fifteen-All"
        elif self.player1_score == 2:
            score_string = "Thirty-All"
        elif self.player1_score == 3:
            score_string = "Forty-All"
        else:
            score_string = "Deuce"
        return score_string

    def get_winning_score_string(self):
        score_difference = self.player1_score - self. player2_score

        if score_difference == 1:
            score_string = "Advantage player1"
        elif score_difference == -1:
            score_string = "Advantage player2"
        elif score_difference >= 2:
            score_string = "Win for player1"
        else:
            score_string = "Win for player2"
        return score_string


    def score_to_text(self, temp_score: int) -> str:
        if temp_score == 0:
            score_string = "Love"
        elif temp_score == 1:
            score_string = "Fifteen"
        elif temp_score == 2:
            score_string = "Thirty"
        elif temp_score == 3:
            score_string = "Forty"
        return score_string

    def get_playing_score_string(self) -> str:
         score = "-".join([self.score_to_text(self.player1_score), self.score_to_text(self.player2_score)])
         return score

    def get_score(self) -> str:

        if self.player1_score == self.player2_score:
            score_string = self.get_tie_score_string()
        elif self.player1_score > self.points or self.player2_score > self.points:
            score_string = self.get_winning_score_string()
        else:
            score_string = self.get_playing_score_string()

        return score_string
