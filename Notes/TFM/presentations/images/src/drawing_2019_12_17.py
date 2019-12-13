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
        self.show_possible_executions(tasks)
        self.show_schedules(tasks)

        self.wait(5)

    def show_possible_executions(self, tasks: List[List[List[int]]]):
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

    def show_schedules(self, tasks: List[List[List[int]]]):
        core = 0
        recs = []
        for task, color in zip(tasks, self.colors):
            rec = self.create_coords_rec(task[0][0], task[0][1], color)
            rec.move_to(self.coords_to_point(task[0][0]/2, task[0][1]/2 + core))
            recs.append(rec)
            core += task[0][1]
            self.bring_to_back(rec)
            self.play(Write(rec))
            self.wait(1)

        # Create possible task sets
        task_sets = self.get_schedules(tasks)
        print(task_sets
              )

        new_rec = [
            self.create_coords_rec(tasks[0][1][0], tasks[0][1][1], self.colors[0]),
            self.create_coords_rec(tasks[1][0][0], tasks[1][0][1], self.colors[1]),
        ]
        new_rec[0].move_to(self.coords_to_point(tasks[0][1][0]/2, tasks[0][1][1]/2))
        new_rec[1].move_to(self.coords_to_point(tasks[1][0][0]/2, tasks[1][0][1]/2 + tasks[0][1][1]))
        self.play(Transform(recs[0], new_rec[0]), Transform(recs[1], new_rec[1]))

    def create_coords_rec(self, width: Num, height: Num, color: str = "#000000",
                          color_stroke: str = "#000000") -> Rectangle:
        point = self.coords_to_point(width, height)
        point -= self.coords_to_point(0, 0)
        rec = Rectangle(width=point[0], height=point[1], color=color)
        rec.set_stroke(color_stroke, opacity=1.)
        rec.set_fill(color, opacity=1.)
        return rec

    def get_schedules(self, tasks: List[List[List[int]]], task: int = 0, sched: List[List[int]] = None, cores = 0) -> List[List[List[int]]]:
        if sched is None:
            sched = []
        if cores > 4:
            return []
        elif task == len(tasks):
            return [sched]

        all_schedules = []
        for i, opts in enumerate(tasks[task]):
            all_schedules += self.get_schedules(tasks, task + 1, sched + [[task, i]], cores + opts[1])

        return all_schedules


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    os.system(f"manim --leave_progress_bars -p -m -c white {module_name} {sys.argv[1]}")
