from draw_with_keyboard import turtle_draw
from turtle_race import turtle_race

if __name__ == "__main__":
    user_choice = 0
    while user_choice not in (1, 2):
        print("1-turtle race\n2-turtle draw")
        user_choice = int(input("which turtle game you want to play? : "))
    if user_choice == 1:
        turtle_race()
    else:
        turtle_draw()
