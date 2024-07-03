from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        start_x = 0
        for segment in range(0, 3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=start_x, y=0)
            self.segments.append(new_segment)
            start_x -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].fd(20)
        self.segments[0].right(90)


