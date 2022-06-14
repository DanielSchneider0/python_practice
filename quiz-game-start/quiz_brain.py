class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def game_continue(self):
        can_continue = True
        if self.question_number == self.question_list[-1]:
            can_continue = False
        return can_continue

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q{self.question_number}. {current_question.text} (True/False)?: "
        ).lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("Correct!")

        else:
            print("That's wrong.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")
