import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}-{alternative}")

    user_choice = int(input("Enter your anwser: "))
    question["user_choice"] = user_choice


for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    match result:
        case 'Correct Answer':
            print(f"Question: {index + 1} is {question['user_choice']}, Good job!")
        case 'Wrong Answer':
            print(f"Question: {index + 1} is not {question['user_choice']}, \
the correct answer is {question['correct_answer']}!")

    #message = f"Question: {index + 1} {result}: {question['user_choice']}, \
    #Correct answer: {question['correct_answer']}"

    #print(message)


percent = int((score/len(data)) * 100)

print(f"You scored {score}/{len(data)}! {percent}%")

