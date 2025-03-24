class QuizBrain:
    def __init__(self, qb_question_list):
        self.question_number = 0
        self.question_list = qb_question_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = str(input(f"Q.{self.question_number} {current_question.text} True/False "))
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Good Job!")
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("Better luck next time!")
            print(f"Your final score was {self.score}/{self.question_number}")
        print(f"Correct answer was {correct_answer}")