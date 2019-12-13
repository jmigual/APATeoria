from typing import List, Union
Num = Union[int, float]

from manimlib.imports import *


class GangAnimation(GraphScene):

    CONFIG = {
        "x_min": 0,
        "x_max": 15,
        "y_min": 0,
        "y_max": 4,
        "y_axis_height": 3,
        "x_axis_label": "Time",
        "y_axis_label": "Core",
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = []

    def construct(self):

        self.colors = ["#67EB34", "#F269FF"]

        self.setup_axes(animate=True)
        self.play(
            ApplyMethod(self.x_axis_label_mob.set_color, "#000000"),
            ApplyMethod(self.y_axis_label_mob.set_color, "#000000")
        )
        self.play(ApplyMethod(self.y_axis_label_mob.shift, 1.5*LEFT))

        tasks = [[[5, 3], [7.5, 2], [15, 1]], [[6, 2], [12, 1]]]

        for task, color in zip(tasks, self.colors):
            main_rec = None
            for width, height in task:
                rec = self.create_coords_rec(width, height, color)
                rec.move_to(self.coords_to_point(width/2, height/2))
                if main_rec is not None:
                    self.play(Transform(main_rec, rec))
                else:
                    main_rec = rec
                    self.bring_to_back(main_rec)
                    self.play(Write(rec))
                self.wait(1)
            self.play(FadeOut(main_rec))

        # main_rec = self.show_first_gangs()
        #
        # task_2 = [6, 2]
        # task_2_rec = self.create_coords_rec(task_2[0], task_2[1], self.colors[1])
        # task_2_rec.move_to(self.coords_to_point(task_2[0]/2, 3 + task_2[1]/2))
        # self.bring_to_back(task_2_rec)
        # self.play(ShowCreation(task_2_rec))

    def show_first_gangs(self) -> Rectangle:
        gang_tasks = [[5, 3], [7.5, 2], [15, 1]]

        original_rec = None
        main_rec = None
        for width, height in gang_tasks:
            rec = self.create_coords_rec(width, height, self.colors[0])
            rec.move_to(self.coords_to_point(width/2, height/2))
            self.bring_to_back(rec)
            if main_rec is not None:
                self.play(Transform(main_rec, rec))
            else:
                original_rec = rec.deepcopy()
                self.remove(original_rec)
                main_rec = rec
                self.play(Write(rec))

            self.wait(2)

        self.play(Transform(main_rec, original_rec))
        return main_rec

    def create_coords_rec(self, width: Num, height: Num, color: str = "#000000") -> Rectangle:
        point = self.coords_to_point(width, height)
        point -= self.coords_to_point(0, 0)
        rec = Rectangle(width=point[0], height=point[1], color=color)
        rec.set_fill(color, opacity=1.)
        return rec


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    os.system(f"manim -p -m -c white {module_name} {sys.argv[1]}")
