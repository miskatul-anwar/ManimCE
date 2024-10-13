from manim import *
from manim.utils.color.XKCD import PALEBLUE
import numpy as np
from numpy._core import records

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 9
config.frame_width = 16


class RosePattern(VMobject):
    def __init__(self, radius=2, k=10, theta_range=TAU, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.k = k
        step_size = 0.05
        theta = np.arange(0, theta_range + step_size, step_size)

        # Calculate points based on the parametric rose curve formula
        points = [
            [
                radius * np.cos(k * t) * np.cos(t),
                radius * np.cos(k * t) * np.sin(t),
                0,  # Z-coordinate, since this is a 2D curve
            ]
            for t in theta
        ]

        # Set points smoothly for smooth curve drawing
        self.set_points_smoothly(points)


class RosePatternScene(Scene):
    def construct(self):
        title = Text(
            "Pookie \ue712 ",
            color=BLUE_C,
            font_size=62,
            fill_opacity=1,  # Opacity values should be between 0 and 1
            stroke_width=4,
            line_spacing=20,
            font="Maple Mono",
            stroke_color=BLUE_B,
        ).move_to(ORIGIN)

        rectangle = RoundedRectangle(
            height=2, width=5, fill_opacity=0.7, color=BLUE_E, corner_radius=0.5
        ).rotate(0.1)

        text = (
            MathTex(
                "Rose \, Pattern",
            )
            .set_opacity(0.7)
            .set_color(PALEBLUE)
            .move_to(UL * 3 + LEFT)
        )

        rose = RosePattern(
            radius=3, k=15, theta_range=TAU * 2, color=RED_C
        ).set_opacity(0.5)
        plane = NumberPlane().set_color(BLUE_A).set_opacity(0.2)
        ax = (
            Axes(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
            )
            .set_opacity(0.5)
            .set_color(RED_A)
        )
        intro = MathTex("Introducing....").set_color(PALEBLUE)
        self.play(Write(intro), run_time=3)
        self.play(FadeOut(intro), run_time=1)
        self.wait(1)
        self.play(DrawBorderThenFill(plane), run_time=2)
        self.play(Create(ax), run_time=2)
        self.play(Create(rose), run_time=6)
        self.play(Write(text), run_time=3)
        self.wait(1)
        self.play(Transform(text, title), Transform(ax, rectangle), run_time=2)
        self.wait(3)
