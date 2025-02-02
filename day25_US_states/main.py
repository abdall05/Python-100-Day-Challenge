from game_screen import GameScreen
from quiz_manager import QuizManager
from states_writer import StatesWriter

game_screen = GameScreen()

quiz_manager = QuizManager()
states_writer = StatesWriter()

game_is_running = True
while game_is_running:
    state = quiz_manager.user_input()
    answer_is_correct = quiz_manager.evaluate_answer(state)
    if answer_is_correct:
        states_writer.write(state)
    else:
        final_score = quiz_manager.get_score()
        states_number = quiz_manager.get_num_states()
        game_is_running = False
    if quiz_manager.get_score() == quiz_manager.get_num_states():
        game_is_running = False
    game_screen.update()

game_screen.title(f"Game Over! you got {quiz_manager.get_score()}/{quiz_manager.get_num_states()} States Correct")

game_screen.exitonclick()
