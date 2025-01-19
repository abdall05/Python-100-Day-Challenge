class Quiz:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_index = 0
        self.score = 0

    def is_over(self):
        return self.question_index == self.question_bank.get_size()

    def next_question(self):
        question = self.question_bank.get_question(self.question_index)
        self.question_index += 1
        return question

    def formatted_question(self, question):
        return f"Q.{self.question_index}: {question.get_text()} (True/False)?: "

    def prompt_question(self, question):
        user_answer = ""
        while user_answer not in ["true", "false"]:
            user_answer = input(self.formatted_question(question)).lower()
        return user_answer

    def evaluate_answer(self, question, user_answer):
        if question.get_answer().lower() == user_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {question.get_answer()}")
        print(f"Your current score is: {self.score}/{self.question_index}\n")

    def display_final_result(self):
        print(f"The Quiz is over!\nYour final score is: {self.score}/{self.question_index}")
