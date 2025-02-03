from turtle import Turtle

import states_extractor

FONT = ("Courier", 8, "bold")

class StatesWriter:
    def __init__(self):
        self.states = set()

    def write(self, state):
        if state in self.states:
            return
        self.states.add(state)
        state_text = Turtle()
        state_text.hideturtle()
        state_text.penup()
        text_position = states_extractor.get_coordinate(state)
        state_text.goto(text_position)
        state_text.write(state,align="center", font=FONT)


