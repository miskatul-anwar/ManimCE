from manim import *
from manim.utils.color.XKCD import GREENISHBLUE


class Graph(Scene):
    def construct(self):
        plane = (
            NumberPlane(
                x_range=[-4, 4, 2],
                y_range=[0, 16, 4],
                y_length=8,
            )
            .set_opacity(0.2)  # Set opacity for the background grid
            .to_edge(DOWN)
            .add_coordinates()
        )
        # Axis labels
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        # Parabola graph and function label
        parab = plane.plot(lambda x: x**2, x_range=[-4, 4], color=GREENISHBLUE)
        func_label = MathTex(r"f(x) = x^2").scale(0.5).next_to(parab, UR, buff=0.5)

        # Title adjustments
        title = (
            Text(
                "Datavis",
                font_size=18,
            )
            .set_color(RED)
            .set_opacity(0.7)  # Title opacity for visibility
            .to_edge(UL)  # Ensure the title stays at the top of the scene
        )

        # Riemann rectangles
        area = plane.get_riemann_rectangles(
            graph=parab, x_range=[-2, 3], dx=0.2, stroke_width=0.1, stroke_color=WHITE
        )

        # Animation sequence
        self.wait(1)
        self.play(DrawBorderThenFill(plane), run_time=3)
        self.play(Create(VGroup(labels, parab, func_label)), run_time=4)
        self.play(DrawBorderThenFill(title), run_time=2)
        self.play(Create(area), run_time=2)
        self.wait(5)
