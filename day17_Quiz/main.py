from data import question_data
from question_model import QuestionBank
from quiz_brain import Quiz

questions_bank = QuestionBank()
questions_bank.add_questions(question_data)
quiz = Quiz(questions_bank)

while not quiz.is_over():
    question = quiz.next_question()
    user_answer = quiz.prompt_question(question)
    quiz.evaluate_answer(question, user_answer)

quiz.display_final_result()


