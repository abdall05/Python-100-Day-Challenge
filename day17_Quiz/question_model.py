import random


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def get_answer(self):
        return self.answer

    def get_text(self):
        return self.text


class QuestionBank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_question(self, question_index):
        return self.questions[question_index]

    def add_questions(self, question_data):
        for question in question_data:
            question_object = Question(question["text"], question["answer"])
            self.add_question(question_object)
        self.shuffle_questions()

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def get_questions(self):
        return self.questions

    def get_size(self):
        return len(self.questions)
