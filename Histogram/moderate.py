from manim import *


class CustomHistogram(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 7, 1], y_range=[0, 25, 5], axis_config={"include_numbers": True}
        )

        # Example data for histogram
        data = [5, 10, 15, 20, 12, 8]

        # Create bars for the histogram
        bars = VGroup()
        for i, value in enumerate(data):
            bar = Rectangle(width=0.8, height=value, fill_color=BLUE, fill_opacity=0.75)
            bar.next_to(axes.c2p(i + 1, 0), UP, buff=0)
            bars.add(bar)

        # Animate axes and bars
        self.play(Create(axes))
        self.play(
            LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.1)
        )
        self.wait(2)
