def print_question(question: dict):
    print(question["text"])
    for i in range(0, len(question["values"])):
        print(f"{i + 1}. {question['values'][i]}")


def ask() -> int:
    user_answer_str = None
    while user_answer_str == None:
        user_answer_str = input("What is your answer? Please enter the number. \n")
        try:
            user_answer = int(user_answer_str)
            return user_answer
        except:
            print("Please enter a number.")


def finish(final_score: int, total_score: int):
    print(f"Your score is: {final_score} out of {total_score}")


question1 = {
    "text": "Who is the odd one out of Sigma Staff?",
    "values": ["Harry", "Sonali", "Chris"],
    "answer": 1,
}

question2 = {
    "text": "What is Chris' surname?",
    "values": ["John", "Owen", "Gaston"],
    "answer": 2,
}

question3 = {
    "text": "What is the capital of China?",
    "values": ["Beijing", "Shanghai", "Taipei"],
    "answer": 1,
}

question4 = {
    "text": "What is the tallest mountain?",
    "values": ["k2", "Mauna Kea", "Everest"],
    "answer": 3,
}

round1 = {"name": "Sigma Labs", "questions": [question1, question2]}

round2 = {"name": "Geography", "questions": [question3, question4]}

rounds = [round1, round2]


def play():
    score = 0

    no_questions = 0
    for round in rounds:
        for question in round["questions"]:
            no_questions += 1
            print_question(question)
            answer = ask()
            is_correct = answer == question["answer"]
            if is_correct:
                score += 1
                print("Correct")
            else:
                print("Incorrect")

    finish(score, no_questions)


play()
