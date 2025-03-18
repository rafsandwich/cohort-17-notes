class Player:
    """A player that plays the game"""
    def __init__(self, name: str):
        """Constructs"""
        self.score = 0
        self.name = name

class Question:
    def __init__(self, text: str, possible_answers: list[str], answer):
        self.text = text
        self.possible_answers = possible_answers
        self.answer = answer

class Round:
    def __init__(self, topic: str, questions: list[Question]):
        self.questions = questions
        self.topic = topic


question1 = Question("Who is the odd one out of Sigma Staff?", ["Harry", "Sonali", "Chris"], 1)

round1 = Round("Sigma Labs", [question1])

print(round1.questions[0].text)
