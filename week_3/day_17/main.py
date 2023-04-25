from data import list_of_questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in list_of_questions:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(
    f"You have completed the quiz. Your final score was: {quiz.score}/{quiz.question_number}"
)
