from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank =[]
for items in question_data:
  question_text = items["text"]
  question_ans = items["answer"]
  new_question = Question(question_text, question_ans)
  question_bank.append(new_question)

quiz = Quiz_brain(question_bank)
while quiz.still_has_question():
  quiz.next_question()

