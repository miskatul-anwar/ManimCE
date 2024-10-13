from manim import *


class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(
            lambda: SurroundingRectangle(
                num, color=BLUE_A, fill_opacity=0.4, fill_color=BLUE_D, buff=0.5
            )
        )
        name = always_redraw(lambda: Tex("Miskat").next_to(box, DOWN, buff=0.25))
        self.play(Create(VGroup(num, box, name)))
        self.play(VGroup(num, box).animate.shift(RIGHT * 2), run_time=2)
        self.wait(2)
