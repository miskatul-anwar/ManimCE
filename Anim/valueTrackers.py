from manim import *


class ValTrackers(Scene):
    def construct(self):
        k = ValueTracker(0)
        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))
        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(1), run_time=5, rate_func=lambda t: t**20 + 1)
