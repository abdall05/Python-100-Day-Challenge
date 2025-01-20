from turtle import Turtle, Screen

is_moving = False
key_sequence = []


def move(turtle, direction):
    global is_moving
    if is_moving:
        return
    is_moving = True

    key_sequence.append(direction)

    if direction == "Forwards":
        turtle.forward(10)
    elif direction == "Backwards":
        turtle.back(10)
    elif direction == "Clockwise":
        turtle.right(15)
        turtle.forward(10)
    elif direction == "Counter-clockwise":
        turtle.left(15)
        turtle.forward(10)

    is_moving = False


def reverse_move(turtle, direction):
    if direction == "Forwards":
        turtle.back(10)
    elif direction == "Backwards":
        turtle.forward(10)
    elif direction == "Clockwise":
        turtle.back(10)
        turtle.left(15)
    else:
        turtle.back(10)
        turtle.right(15)


def clear(turtle):
    global key_sequence
    turtle.pencolor("white")
    turtle.speed(0)  # fastest
    for direction in reversed(key_sequence):
        reverse_move(turtle, direction)

    key_sequence.clear()
    turtle.pencolor("blue")
    turtle.speed(6)  # normal


def turtle_draw():
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.pencolor("blue")
    screen = Screen()

    screen.onkey(lambda: move(turtle, "Forwards"), "w")
    screen.onkey(lambda: move(turtle, "Clockwise"), "d")
    screen.onkey(lambda: move(turtle, "Counter-clockwise"), "a")
    screen.onkey(lambda: move(turtle, "Backwards"), "s")
    screen.onkey(lambda: clear(turtle), "c")

    screen.listen()
    screen.mainloop()
