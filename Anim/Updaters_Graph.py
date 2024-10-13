from manim import *
from manim.utils.color.X11 import GREEN2


class UpdatersGraph(Scene):
    def construct(self):
        # Create the axes
        ax = Axes(
            x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10, y_length=6
        ).to_edge(DOWN)

        # Define the quadratic function graph
        func = ax.get_graph(
            lambda x: x**2,
            x_range=[-4, 4],
            color=BLUE,
        )

        # Create the initial secant slope group
        slope = ax.get_secant_slope_group(
            x=0,  # Start at x = 0
            graph=func,
            dx=0.01,
            secant_line_color=GREEN2,
            secant_line_length=3,
        )

        # Create a dot to track the secant line's position
        dot = Dot(ax.c2p(0, 0), color=YELLOW)

        # Updater function to animate the secant slope
        def update_slope(mob, dt):
            # Update the secant slope group dynamically
            mob.become(
                ax.get_secant_slope_group(
                    x=mob.x_val,
                    graph=func,
                    dx=0.01,
                    secant_line_color=GREEN2,
                    secant_line_length=3,
                )
            )
            # Increase the x value to move the secant line
            mob.x_val += dt * 0.5  # Adjust the speed of movement
            if mob.x_val >= 3:  # Stop the updater at x = 3
                mob.x_val = 3
                mob.remove_updater(update_slope)

        def update_dot(dot):
            dot.move_to(ax.c2p(slope.x_val, func.underlying_function(slope.x_val)))

        slope.x_val = -3  # Starting at x = -3

        slope.add_updater(update_slope)
        dot.add_updater(update_dot)

        # Add everything to the scene
        self.add(ax, func, slope, dot)
        self.wait(8)  # Control the animation duration
