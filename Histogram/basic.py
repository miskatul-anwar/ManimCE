from manim import *
from manim.utils.color.XKCD import NAVYGREEN, PALEGREY


class HistogramExample(Scene):
    def construct(self):
        # Example data for histogram
        data = [5, 10, 15, 20, 12, 8]

        # Create a bar chart (a histogram in this case)
        histogram = BarChart(
            values=data,  # The data for the histogram
            bar_colors=[
                BLUE,
                RED,
                GREEN,
                YELLOW,
                TEAL,
                PALEGREY,
            ],  # Color for the bars
            y_range=[0, 25, 5],  # Range for the y-axis
            bar_width=0.6,  # Width of each bar
            bar_names=[f"Bin {i+1}" for i in range(len(data))],  # Names for each bin
        )

        # Animate the appearance of the histogram
        self.play(Create(histogram))
        self.wait(2)
