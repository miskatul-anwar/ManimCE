from manim import *
import pandas as pd
import numpy as np


class PieChartExample(Scene):
    def construct(self):
        try:
            # Read the CSV file
            df = pd.read_csv("data.csv")
        except FileNotFoundError as e:
            print(e, "File not found! ⭐")
            return  # Exit if the file is not found

        # Data for pie chart
        values = df["length"].to_list()
        labels = df["species"].to_list()

        # Normalize the values to create proportional slices
        total = sum(values)
        angles = [360 * (v / total) for v in values]

        # Start drawing pie chart
        start_angle = 90
        radius = 2

        # Colors for the pie chart (using global valid Manim colors)
        colors = [globals().get(color, BLUE) for color in df["color"].to_list()]

        # Create and display each slice of the pie
        for i, angle in enumerate(angles):
            # Create a slice of the pie
            pie_slice = Sector(
                start_angle=start_angle * DEGREES,
                angle=angle * DEGREES,
                outer_radius=radius,
                fill_color=colors[i],
                fill_opacity=0.8,
            )
            self.add(pie_slice)

            # Add label for each slice
            label = Text(labels[i]).move_to(pie_slice.point_from_proportion(0.5))
            self.add(label)

            start_angle += angle

        # Animation to display the pie chart
        self.wait(2)
