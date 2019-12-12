from typing import List

from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3*TAU/8)
        circle.set_fill(PINK, opacity=.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class GangAnimation(GraphScene):

    CONFIG = {
        "x_min": -1,
        "x_max": 20,
        "y_min": -1,
        "y_max": 10,
        "x_axis_label": "Time",
        "y_axis_label": "Core"
    }

    def construct(self):
        self.setup_axes(animate=True)
        # self.play(Transform(self.x_axis_label_mob, self.x_axis_label_mob.set_fill(BLACK)))
        self.play(
            Transform(self.x_axis_label_mob, self.x_axis_label_mob.set_color(BLACK)),
            Transform(self.y_axis_label_mob, self.y_axis_label_mob.set_color(BLACK))
        )

        core_usage = [[0, 10], [0, 7], [0, 7], [0, 5]]
        self.draw_cores(core_usage)

    def draw_cores(self, cores: List[List[int]]):
        core = 0

        for [cmin, cmax] in cores:
            coords = self.coords_to_point(cmax - cmin, 1)
            coords -= self.coords_to_point(0, 0)
            width, height = coords[0], coords[1]
            print(width, height)
            rec = Rectangle(width=width, height=height, color=BLACK)
            rec.move_to(self.coords_to_point((cmax - cmin)/2, core + .5))
            self.play(FadeIn(rec))
            # rec.set_coord()
            core += 1


