import random as rd
from manim import *
from manim.utils.color.BS381 import RED_OXIDE
from manim.utils.color.X11 import BROWN2, GRAY60, LAVENDERBLUSH3, PALETURQUOISE4
from manim.utils.color.XKCD import (
    BLUEPURPLE,
    BLUEVIOLET,
    BROWNGREEN,
    GREYBROWN,
    MOSSGREEN,
    NEONGREEN,
    ORANGEBROWN,
    ORANGEISH,
    ORANGEYYELLOW,
    PALEBLUE,
    PINEGREEN,
)
from manim.utils.unit import Percent

config.background_color = BLACK
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080


class Crit(Scene):
    def construct(self):
        c = Circle(color=GREYBROWN, fill_opacity=0.5)
        self.play(FadeIn(c))
        colors = [
            RED,
            GREEN,
            BLUE,
            YELLOW,
            RED_OXIDE,
            ORANGEBROWN,
            BLUEVIOLET,
            MOSSGREEN,
            BROWN2,
            NEONGREEN,
            ORANGEISH,
            LAVENDERBLUSH3,
        ]

        directions = [
            (0, 0, 0),
            UP,
            RIGHT,
            UR,
            DR,
            DOWN,
            DL,
            LEFT,
            UL,
        ]
        for d in directions:
            size = len(colors) - 1
            index = rd.randint(0, size)
            self.play(
                Create(
                    (
                        Cross(scale_factor=0.2).move_to(c.get_critical_point(d))
                    ).set_color(colors[index])
                )
            )
        for perc in range(15, 51, 5):
            size = len(colors) - 1
            index = rd.randint(0, size)
            self.play(
                Create(Circle(radius=perc * Percent(X_AXIS)).set_color(colors[index]))
            )
