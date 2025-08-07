questions = ("How do you concatenate two strings in Python?",
             "What is the keyword used to define a function in Python?",
             "As what datatype are the *args stored, when passed into a function?",
             "What is the keyword used to define a class in Python?",
             "What is the keyword used to import modules in Python?")



options =(('A. str1 . str2','B. str1 + str2', 'C. str1 , str2' ,'D. concat(str1, str2)'),
          ("A. def", 'B. function', 'C. func', 'D. define'),
          ('A. list', 'B. tuple','C. Dictionery', 'D. None of the Above' ),
          ('A. class', 'B. def', 'C. function', 'D. method'),
          ('A. import', 'B. include', 'C. require', 'D. load'))


answers =('B', 'A', 'B', 'A', 'A')

guesses =[]
score = 0
question_num = 0

for question in questions:
    print("*********************************")
    print(question)

    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer from options (A/B/C/D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("WRONG!")
        print("The correct answer is: {}".format(answers[question_num]))
    question_num += 1


print("*********************************")
print("RESULTS")
print("Your answers: ", end="")
for i in guesses:
    print(i, end=" ")

print("\nCorrect answers: ", end="")
for i in answers:
    print(i, end=" ")
print()

print("\nYour score is {}/{}".format(score, len(questions)))
if score == len(questions):
    print("Congratulations! You got a perfect score!")
elif score >= len(questions) / 2:
    print("GOOD!, keep more practice")
else:
    print("You need more practice, try again!")

