from manim import *
from manim.utils.color.X11 import BLUE4, GREEN1
from manim.utils.color.XKCD import GREENAPPLE, REDORANGE

config.background_color = BLACK
config.frame_height = 9
config.frame_width = 16
config.pixel_height = 1080
config.pixel_width = 1920


class Getters(Scene):
    def construct(self):
        rect = Rectangle(color=BLUE_A, fill_color=BLUE4, fill_opacity=0.6).to_edge(UL)
        circ = Circle(color=GREENAPPLE, fill_color=REDORANGE, fill_opacity=0.5).to_edge(
            DOWN
        )
        arrow = always_redraw(
            lambda: Line(
                start=rect.get_bottom(), end=circ.get_top(), buff=0.2
            ).add_tip()
        )
        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)
