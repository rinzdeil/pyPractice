import json

with open("text_folder/questions.json", "r") as file:
  content = file.read()

data = json.loads(content)
score = 0
total_score = len(data)

for question in data:
  print(question["question_text"])
  for index, option in enumerate(question["options"]):
    print(f"{index + 1}. {option}")
    
  user_answer = input("Enter your answer: ").capitalize()
  question["user_answer"] = user_answer

for index, question in enumerate(data):
  if question["user_answer"] == question["correct_answer"]:
    score = score + 1
    result = "Correct Answer"
  else:
    result = "Wrong Answer"

  message = f"Question{index + 1}. {question['question_text']} \n{question['user_answer']} is the {result}"
  print(message, f"\n Score: {score} / {total_score}")
   