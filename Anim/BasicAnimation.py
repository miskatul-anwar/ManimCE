from manim import *


class BasicAnimation(Scene):
    def construct(self):
        red_dot = Dot(color=RED, stroke_width=1, radius=0.1).next_to([0, 0, 0], RIGHT)
        circle = Circle(color=GREEN, radius=0.5).move_to([3, 2, 1])
        plane = NumberPlane()
        square = Square(color=YELLOW).move_to([5, 2, 1])
        self.add(plane, red_dot, circle, square)
