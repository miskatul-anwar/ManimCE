from manim import *
from numpy import True_


class Plot(ThreeDScene):
    def construct(self):
        ax = Axes(x_range=(-3, 3, 1), y_range=(-3, 3, 1))
        title = Text(
            "Pookie \ue712 ",
            should_center=True,
            color=BLUE_C,
            font_size=62,
            fill_opacity=5,
            stroke_width=4,
            line_spacing=20,
            font="CaskaydiaCove Nerd Font",
            stroke_color=BLUE_B,
        )
        plane = NumberPlane().set_color(BLUE_A).set_opacity(0.2)
        curve = ax.plot(lambda x: (x + 2) * x * (x - 2) / 2, color=RED)
        curve2 = ax.plot(lambda x: (2 * x + 2) * x * (2 * x - 2) / 2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0))
        area2 = ax.get_area(curve2, x_range=(0, 1.5))
        rectangle = RoundedRectangle(
            height=2.5, width=7, fill_opacity=0.6, color=BLUE_D, corner_radius=0.5
        ).rotate(0.1)
        tri1 = Triangle().set_color(RED_A).set_opacity(0.2).to_corner()
        cube2 = Cube().set_color(GREEN).set_opacity(0.2).to_corner(UP + RIGHT)
        cir1 = Circle().set_color(YELLOW_A).set_opacity(0.2).to_corner()
        cir2 = Circle().set_color(GREEN).set_opacity(0.2).to_corner(UP + RIGHT)

        # self.add(ax, curve, area)
        self.play(FadeIn(ax), run_time=1)
        self.play(Create(curve), Create(area), run_time=2)
        self.play(Transform(ax, rectangle), run_time=2)
        self.play(DrawBorderThenFill(title), run_time=2)
        self.play(
            Transform(curve, curve2), Transform(area, area2), FadeIn(plane), run_time=2
        )
        # self.play(Transform(area, area2), run_time=1)
        self.add(tri1, cir2)
        self.wait(0.5)
        self.play(
            Transform(tri1, cir1),
            Transform(cir2, cube2),
            run_time=2,
        )
        self.wait(1)
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.wait(3)
