questions = [
    "What is the capital of the USA?",
    "How many states are there in the USA?",
    "Which city is known as the Big Apple?",
    "Who was the first President of the USA?",
    "Which is the largest state in the USA?",
    "Which ocean is on the east coast of the USA?",
    "Which state is known as the Sunshine State?",
    "Which American city is famous for the Golden Gate Bridge?"
]
answers = [
    "Washington D.C.",
    "50",
    "New York",
    "George Washington",
    "Alaska",
    "Atlantic Ocean",
    "Florida",
    "San Francisco"
]
prizes = [1000, 5000, 10000, 50000, 100000, 250000, 500000, 1000000]
amount=0
print("================================")
print("      THE AMERICAN QUIZ")
print("================================")
for i in range(len(questions)):
    print("\nQUESTIONS",i+1)
    print(questions[i])
    user_answer=input("Enter your answer: ")
    if user_answer.lower()==answers[i].lower():
        print("correct Answer!")
        amount=amount+prizes[i]
        print("you won $",prizes[i])
    else:
        print("wrong Answer!")
        print("correct answer was:",answers[i])
        break
print("\n================================")
print("FINAL AMOUNT WON = $", amount)
print("================================")
