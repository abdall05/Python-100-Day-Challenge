import utils


class Snake:
    def __init__(self):
        self.head = utils.create_square()
        self.body = [self.head]
        self.just_grow = False
        self.grow()
        self.grow()

    def grow(self):
        tail = utils.create_square()
        previous_tail = self.body[-1]
        previous_tail_position = previous_tail.position()
        tail.goto(previous_tail_position[0], previous_tail_position[1])
        self.body.append(tail)
        self.just_grow = True

    def bite_it_self(self):
        for segment in self.body[1:]:
            if self.head.distance(segment) < utils.SQUARE_SIZE/2:
                return True
        return False

    def turn(self, direction):
        if direction == 'right':
            self.head.right(90)
        elif direction == 'left':
            self.head.left(90)

    def forward(self):

        previous_position = self.head.pos()
        self.head.forward(utils.SQUARE_SIZE)
        for segment in self.body[1:-1]:
            tmp = segment.pos()
            segment.goto(previous_position)
            previous_position = tmp
        if not self.just_grow:
            if len(self.body) > 1:
                self.body[-1].goto(previous_position)
        else:
            self.just_grow = False

    def positions(self):
        return [elem.pos() for elem in self.body]
