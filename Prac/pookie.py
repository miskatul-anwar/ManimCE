from manim import *
from moderngl_window import run_window_config
from numpy import True_


class Plot(ThreeDScene):
    def construct(self):
        ax = Axes(x_range=(-3, 3, 1), y_range=(-3, 3, 1))
        title = Text(
            "Pookie \ue712 ",
            color=BLUE_C,
            font_size=62,
            fill_opacity=1,  # Opacity values should be between 0 and 1
            stroke_width=4,
            line_spacing=20,
            font="CaskaydiaCove Nerd Font",
            stroke_color=BLUE_B,
        ).move_to(
            ORIGIN
        )  # Centering the text manually

        plane = NumberPlane().set_color(BLUE_A).set_opacity(0.2)

        # Define the curves
        curve = ax.plot(lambda x: (x + 2) * x * (x - 2) / 2, color=RED)
        curve2 = ax.plot(lambda x: (2 * x + 2) * x * (2 * x - 2) / 2, color=RED)

        # Define the areas under the curves
        area = ax.get_area(curve, x_range=(-2, 0))
        area2 = ax.get_area(curve2, x_range=(0, 1.5))

        # Create other objects like rectangle, triangles, circles, and cubes
        rectangle = RoundedRectangle(
            height=2.5, width=7, fill_opacity=0.6, color=BLUE_D, corner_radius=0.5
        ).rotate(0.1)

        cyl1 = (
            Cylinder(direction=[1, 1, 0]).set_color(RED_A).set_opacity(0.2).to_corner()
        )
        cube2 = Cube().set_color(GREEN).set_opacity(0.2).to_corner(UP + RIGHT)
        tri1 = Triangle().set_color(YELLOW_A).set_opacity(0.2).to_corner()
        cir2 = Circle().set_color(GREEN).set_opacity(0.2).to_corner(UP + RIGHT)

        # Animate the objects
        self.play(FadeIn(ax), run_time=1)
        self.play(Create(curve), Create(area), run_time=2)
        self.play(Transform(ax, rectangle), run_time=2)
        self.play(DrawBorderThenFill(title), run_time=2)
        self.add(tri1, cir2)
        self.play(
            Transform(curve, curve2),
            Transform(area, area2),
            FadeIn(plane),
            run_time=2,
        )

        # Adding and transforming 3D objects
        self.play(
            Transform(tri1, cyl1),
            Transform(cir2, cube2),
            run_time=3,
        )
        self.wait(3)
