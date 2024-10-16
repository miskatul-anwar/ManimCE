from manim import *


class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        m1 = Square().set_color(BLUE)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        m3 = Rectangle().set_color(YELLOW).rotate(-0.2)
        self.play(Transform(m1, m2), run_time=5)
        self.play(Transform(m2, m1), run_time=5)
        # self.play(FadeIn(m2), run_time=2)
        # self.play(Transform(m2, m3), run_time=5)
        # self.play(FadeIn(m3), run_time=1)
