class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {question.text} (True/False): "
        ).lower()

        while user_answer != "true" and user_answer != "false":
            user_answer = input("Incorrect answer type. Try again: ").lower()

        self.check_answer(user_answer, question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if correct_answer.lower() == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")

        print(f"The Correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
