import random

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0

    def get_current_question(self):
        return self.questions[self.current_question]

    def check_answer(self, user_answer):
        if user_answer.lower() == self.get_current_question().answer.lower():
            return True
        else:
            return False

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
        else:
            self.current_question += 1  # Move to the next question to indicate the end of the quiz

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points

# Get player name
player_name = input("Enter your name: ")

# Create questions
questions = [
    Question("What is the capital of France?", "Paris"),
    Question("What is the capital of India?", "New Delhi"),
    Question("Which Avenger is red in color and has the mind stone?", "Vision")
]

# Create quiz
quiz = Quiz(questions)

# Create player
player = Player(player_name)

# Conduct quiz
while quiz.current_question < len(quiz.questions):
    current_question = quiz.get_current_question()
    user_answer = input(current_question.question + " ")
    if quiz.check_answer(user_answer):
        print("Correct!")
        player.add_points(1)
    else:
        print(f"Incorrect, the correct answer was {current_question.answer}")

    quiz.next_question()

# Display results
print(f"\n{player.name}, you scored {player.score} out of {len(quiz.questions)}\n")
