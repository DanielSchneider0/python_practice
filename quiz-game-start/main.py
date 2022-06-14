from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_bank = []
for question in question_data:
    selected_question = Question(question["question"], question["correct_answer"])
    q_bank.append(selected_question)

quiz = QuizBrain(q_bank)

while quiz.game_continue:
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
