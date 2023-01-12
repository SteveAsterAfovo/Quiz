import random

questions = {
    "Quelle est la capitale de France?": "Paris",
    "Combien de doigts a une main?": "5",
    "Quel est le plus grand océan du monde?": "Océan Pacifique",
  "Qui est le concepteur de cette application ?": "Steve Aster Afovo"
}

score = 0

for question in questions:
    print(question)
    answer = input()
    if answer == questions[question]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. La réponse était", questions[question])

print("Vous avez", score, "points sur", len(questions))
