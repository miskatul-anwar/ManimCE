from manim import *


class NameOfAnimation(Scene):
    def construct(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6)
        axes.to_edge(LEFT, buff=0.5)
        box = Rectangle(
            stroke_color=GREEN_C,
            stroke_opacity=0.7,
            fill_color=RED_B,
            fill_opacity=0.5,
            height=1,
            width=1,
        )
        self.add(box)
        self.play(box.animate.shift(RIGHT * 2), run_time=2)
        self.play(box.animate.shift(UP * 3), run_time=2)
        self.play(box.animate.shift(DOWN * 5 + LEFT * 5), run_time=2)
        self.play(box.animate.shift(UP * 1.5 + RIGHT * 1), run_time=2)
