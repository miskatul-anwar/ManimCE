from manim import *
from manim.utils.color.X11 import GREEN2

config.background_color = BLACK


class Testing(Scene):
    def construct(self):
        # Define a triangle with three points
        poly = Polygon(
            [-1, 1, 0],
            [1, 1, 0],
            [0, -1, 0],
            [3, 2, 1],
            [5, 2, 1],
            fill_color=GREEN2,
            fill_opacity=0.5,
        )
        self.play(
            Rotate(poly, PI, rate_func=there_and_back),
            run_time=2,
        )
        self.wait(1)
