#!/usr/bin/python3

"""Create a multiple-choice quiz 
    with questions about Python, 
    Display scores at the end and 
    allow the user to play again.
"""

quiz_title = "Simple Python Quiz Game".upper()
print("--------------------------------------------------------------------------------")
print("                             {}                            ".format(quiz_title))

quiz_questions = [
        {
            "question" : "1. What is the correct way to create a list in Python?",
            "options" : {"A": "myList = [1, 2, 3]", "B" : "myList = {1, 2, 3}"},
            "answer" : {"A": "myList = [1, 2, 3]"},
        },

        {
            "question" : "2. What does the following code output?\nx = '123'\nprint(int(x) + 1)",
            "options" : {"A" : "1231", "B" : "124"},
            "answer" : {"B" : "124"},
        },

        {
            "question" : "3. Which of the following methods is used to add an item to a list in Python?",
            "options" : {"A": "list.append(item)", "B" : "list.push(item)"},
            "answer" : {"A" : "list.append(item)"},
        },

        {
            "question" : "4. What is the output of this code snippet?\nprint('Python'[-1])",
            "options" : {"A": "P", "B": "n"},
            "answer" : {"B": "n"},
        }
    ]

while(True):
    score = 0
    
    for quiz in quiz_questions:
        print("--------------------------------------------------------------------------------")
        print(quiz["question"])
        print("--------------------------------------------------------------------------------")

        for key, value in quiz["options"].items():
            print("({}) : {}".format(key,value))
            print("--------------------------------------------------------------------------------")
        print("")
        
        user_answer = input("Enter the correct answer: ")
        
        if (user_answer.upper() or user_answer.lower()) in quiz["answer"].keys():
            score += 25
            print("Correct!\nYou have {}points".format(score))
        elif user_answer in quiz["answer"].values():
            score += 25
            print("Correct!\nYou have {}points".format(score))
        else:
            print("Wrong.")
        
        print("\n")

    score_point = "Hey!, you scored {}points.".format(score)
    print("--------------------------------------------------------------------------------")
    print(score_point)
    print("--------------------------------------------------------------------------------")
    
    print("\n")
    
    replay_option1 = "Yes"
    replay_option2 = "No"
    replay = input("Do you want to play again? Yes|No\n").title()
    
    print("\n")

    if replay == replay_option1:
        continue
    else:
        break