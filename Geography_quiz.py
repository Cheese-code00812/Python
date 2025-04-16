import random

questions = {
    "What is the name of the tallest mountain in the world?":"Mount Everest",
    "Which country has the largest population in the world?":"China",
    "What is the name of the longest river in Africa?":"Nile River",
    "What is the capital of Mexico?":"Mexico City",
    "What is the name of the largest country in the world?":"Russia",
    "Which country is the Eiffel Tower located in?":"France",
    "What is the capital of Canada?":"Ottawa",
    "What is the name of the largest ocean in the world?":"Pacific Ocean",
    "What country are the Great Pyramids of Giza located in?":"Egypt",
    "What is the capital of Thailand?":"Bangkok",
    "What is the name of the smallest country in the world?":"Vatican City",
    "What is the capital of the American State of California?":"Sacramento",
    "What country has the most natural lakes?":"Canada",
    "How many States does the United States consist of?":"50",
    "What planet is closest to Earth?":"Venus",
    "Which country is also called The Netherlands?":"Holland"
}

question_count = 1

def question_gen():
    question = random.choice(list(questions.keys()))
    answer = questions[question]
    del questions[question]
    return question, answer

def main():
    global question_count
    q, a = question_gen()
    
    print(f"{question_count}. {q}")
    user_answer = input("Enter your answer here: ").strip()
    question_count += 1
    
    return user_answer.lower() == a.lower(), a
  
correct_answers = 0

while question_count <= 15 and questions:
    correct, actual_answer = main()
    
    if correct:
        print("Great job! That's correct!")
        correct_answers += 1
    else:
        print(f"Better luck next time! The correct answer was: {actual_answer}")

score = (correct_answers/15) * 10

print(f"your accuracy score was {score:.2f}%")
