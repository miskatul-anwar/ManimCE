from manim import *
import pandas as pd


class Histogram(Scene):
    def construct(self):
        try:
            df = pd.read_csv("data.csv")
        except FileNotFoundError as e:
            print(e, "File not found! ⭐")
            return

        colors = [globals().get(color, BLUE) for color in df["color"].to_list()]

        histogram = BarChart(
            values=df["length"].to_list(),
            bar_colors=colors,
            y_range=[0, 10, 1],
            bar_width=0.6,
            bar_names=df["species"].to_list(),  # Names for each bin (x-axis labels)
        )

        # Play animation to create the histogram
        self.play(Create(histogram))
        self.wait(2)
