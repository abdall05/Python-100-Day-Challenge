import turtle

import states_extractor


class QuizManager:
    def __init__(self):
        self.states = states_extractor.get_states()
        self.guessed_states = set()
        self.score = 0
        self.num_states = len(self.states)

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score
    def get_num_states(self):
        return self.num_states

    def user_input(self):
        if self.score == 0:
            prompt = "Enter a state name"
        else:
            prompt = "What's another state name?"

        title = f"{self.score}/{self.num_states} States Correct"
        answer = turtle.textinput(title, prompt).lower()
        return answer

    def evaluate_answer(self, answer):
        if answer not in self.states:
            return False
        else:
            if answer not in self.guessed_states:
                self.increment_score()
                self.guessed_states.add(answer)
            return True
