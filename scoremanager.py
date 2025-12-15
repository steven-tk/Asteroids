import json
from constants import SCORE_FILE, MAX_SCORES, PLAYER_NAME



class ScoreManager:
    def __init__(self,):
        self.file = SCORE_FILE
        self.max_scores = MAX_SCORES
        self.scores = []
        self.load_file()

    def load_file(self):
        if not self.file.exists():
            self.scores = []
            return

        with open(self.file, "r") as json_file:
            data = json.load(json_file)
            self.scores = data.get("scores", [])

    def add_score(self, score):
        self.scores.append({
            "name": PLAYER_NAME,
            "score": score
        })

        self.scores.sort(key=lambda s: s["score"], reverse=True)
        self.scores = self.scores[:self.max_scores]

    def save_file(self):
        with open(self.file, "w") as json_file:
            json.dump({"scores": self.scores}, json_file, indent=2)

    def get_scores(self):
        return self.scores

    def print_highscores(self):
        print("===== Current Highscores =====")
        for i, entry in enumerate(self.scores, start=1):
            print(f"{i:>3}. {entry['score']:>5} - {entry['name']}")


                                    

Score = ScoreManager()