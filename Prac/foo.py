from manim import *


class FirstExample(Scene):
    def construct(self):
        blue_circle = Circle(color=RED, fill_opacity=0.5)
        green_square = Square(color=BLUE, fill_opacity=0.8)
        green_square.rotate(0.25)
        self.play(FadeIn(green_square))
        self.play(
            Transform(green_square, blue_circle),
            run_time=5,
        )
        self.play(FadeOut(blue_circle))
        self.play(Transform(blue_circle, green_square))
