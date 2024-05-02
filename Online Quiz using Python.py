import random

quiz = {
    '1': {'question': 'What is the capital of France?', 'answer': 'Paris'},
    '2': {'question': 'What is the capital of India?', 'answer': 'New Delhi'},
    '3': {'question': 'Which Avenger is red in color and has the mind stone?', 'answer': 'Vision'}
}

def check_answers(quiz):
    score = 0
    print("Welcome to the Quiz!")
    print("--------------------")
    for q in quiz:
        print(quiz[q]['question'])
        user_answer = input("Your answer: ")
        quiz[q]['check'] = user_answer
        if quiz[q]['answer'] == quiz[q]['check']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect, the correct answer was {quiz[q]['answer']}\n")
    print(f"\nYou scored {score} out of {len(quiz)}\n")

random.shuffle(list(quiz.keys()))

check_answers(quiz)