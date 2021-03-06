from typing import List, Union, Tuple

Num = Union[int, float]
Coord = Tuple[Num, Num]

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
        # self.y_axis_label_mob.shift(1.5*LEFT)
        y_axis_label = self.y_axis_label_mob.copy()
        y_axis_label.set_color("#000000")
        y_axis_label.shift(1.5*LEFT)
        self.play(
            ApplyMethod(self.x_axis_label_mob.set_color, "#000000"),
            Transform(self.y_axis_label_mob, y_axis_label),
        )
        # self.play()

        tasks = [[[5, 3], [7.5, 2], [15, 1]], [[6, 2], [12, 1]]]
        self.show_possible_executions(tasks)
        self.show_schedules(tasks)

        self.wait(5)

    def show_possible_executions(self, tasks: List[List[List[int]]]):
        for task, color in zip(tasks, self.colors):
            main_rec = None
            main_text = None
            for width, height in task:
                rec = self.create_coords_rec(width, height, color)
                text = TextMobject(f"{height} threads" if height > 1 else f"{height} thread")
                text.set_color("#000000")
                rec.move_to(self.coords_to_point(width/2, height/2))
                text.move_to(self.coords_to_point(width/2, height/2))
                if main_rec is not None:
                    self.play(Transform(main_rec, rec), Transform(main_text, text))
                else:
                    main_rec = rec
                    main_text = text
                    self.bring_to_back(main_rec)
                    self.play(Write(rec), ShowCreation(text))
                self.wait(1)
            self.play(FadeOut(main_rec), FadeOut(main_text))

    def show_schedules(self, tasks: List[List[List[int]]]):
        # Draw how every task is added to the pile
        core = 0
        recs = []
        texts = []
        for task, color in zip(tasks, self.colors):
            width, height = task[0]
            rec = self.create_coords_rec(width, height, color)
            point = self.coords_to_point(width/2, height/2 + core)
            rec.move_to(point)
            recs.append(rec)
            self.bring_to_back(rec)

            text = TextMobject(f"${width} \\times {height} = {width*height:.0f}$")
            text.set_color("#000000")
            text.move_to(point)
            texts.append(text)

            core += height
            self.play(Write(rec), Write(text))
            self.wait(1)

        # Draw tasks in sequence
        transforms = []
        time_value = 0
        max_time = 0
        used_resources = 0
        for task, color, rec, text in zip(tasks, self.colors, recs, texts):
            width, height = task[0]
            new_rec = self.create_coords_rec(width, height, color)
            point = self.coords_to_point(width/2 + time_value, height/2)
            new_rec.move_to(point)
            transforms.append(Transform(rec, new_rec))

            new_text = TextMobject(f"{width*height:.0f}")
            new_text.set_color("#000000")
            new_text.move_to(point)
            transforms.append(Transform(text, new_text))

            time_value += width
            max_time = max(max_time, time_value)
            used_resources += width*height

        # rec_slack = self.create_coords_rec(max_time, 4)
        # rec_slack.move_to(self.coords_to_point(max_time/2, 4/2))
        # self.bring_to_back(rec_slack)
        # transforms.append(FadeIn(rec_slack))

        # text_slack = TextMobject(f"Slack: {4*max_time - used_resources:.0f}")
        # text_slack.set_color("#000000")
        # text_slack.move_to(self.coords_to_point(7.5, 5))
        # transforms.append(FadeIn(text_slack))

        self.play(*transforms)
        self.wait(2)

        # Draw all the possible task sets
        task_sets = self.get_schedules(tasks)
        for task_set in task_sets:
            core = 0
            transforms = []
            max_time = 0
            used_resources = 0
            for [task_id, subtask_id], rec, text in zip(task_set, recs, texts):
                width, height = tasks[task_id][subtask_id]
                new_rec = self.create_coords_rec(width, height, self.colors[task_id])
                point = self.coords_to_point(width/2, height/2 + core)
                new_rec.move_to(point)
                transforms.append(Transform(rec, new_rec))

                new_text = TextMobject(f"{width*height:.0f}")
                new_text.set_color("#000000")
                new_text.move_to(point)
                transforms.append(Transform(text, new_text))

                core += height
                max_time = max(max_time, width)
                used_resources += width*height

            # new_rec_slack = self.create_coords_rec(max_time, 4)
            # new_rec_slack.move_to(self.coords_to_point(max_time/2, 4/2))
            # transforms.append(Transform(rec_slack, new_rec_slack))

            # new_text_slack = TextMobject(
            #     f"Slack: {4*max_time:.0f} - {used_resources:.0f} = {4*max_time - used_resources:.0f}")
            # new_text_slack.set_color("#000000")
            # new_text_slack.move_to(self.coords_to_point(7.5, 5))
            # transforms.append(Transform(text_slack, new_text_slack))

            self.play(*transforms)
            self.wait(1)

        self.wait(1)

    def create_coords_rec(self, width: Num, height: Num, color: str = "#000000",
                          color_stroke: str = "#000000") -> Rectangle:
        point = self.coords_to_point(width, height)
        point -= self.coords_to_point(0, 0)
        rec = Rectangle(width=point[0], height=point[1], color=color)
        rec.set_stroke(color_stroke, opacity=1.)
        rec.set_fill(color, opacity=1.)
        return rec

    def get_schedules(self, tasks: List[List[List[int]]], task: int = 0, sched: List[List[int]] = None, cores=0) -> \
            List[List[List[int]]]:
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


class ElasticButtazzo(Scene):
    CONFIG = {
        "x_min": 0,
        "x_max": 15,
        "y_min": 0,
        "y_max": 4,
        "x_axis_width": 10,
        "y_axis_height": 3,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = []
        self.x_min: float = 0
        self.x_max: float = 0
        self.y_min: float = 0
        self.y_max: float = 0
        self.x_axis_width: float = 0
        self.y_axis_height: float = 0

    def construct(self):
        self.colors = ["#67EB34", "#F269FF"]
        objects = []

        uti_height = -1
        uti_width = 8
        uti_offset = 3.5

        # Utilization line
        line_uti = self.create_coords_line((uti_offset, uti_height), (uti_width + uti_offset, uti_height))
        objects.append(line_uti)

        # 1 utilization
        line_uti_1 = self.create_coords_line((uti_width + uti_offset, uti_height),
                                             (uti_width + uti_offset, uti_height + 1.5), "#ff0000")
        objects.append(line_uti_1)
        text_uti = TextMobject("1", color=COLOR_MAP["BLACK"])
        text_uti.move_to(self.coords_to_point(uti_width + uti_offset, uti_height - .5))
        objects.append(text_uti)

        self.play(ShowCreation(VGroup(*objects)))

        # Show tasks and its utilization
        tasks = [[5, 10], [6, 10]]
        time_line = 0
        height = 2
        recs = []
        recs_uti = []
        vecs_deadline = []
        x_uti = uti_offset
        first = True
        for task, color in zip(tasks, self.colors):
            animations = []
            line = self.create_coords_line((self.x_min, height), (self.x_max, height))

            rec_width, rec_height = task[0], .7
            rec = self.create_coords_rec(rec_width, rec_height, color)
            self.bring_to_back(rec)
            rec.move_to(self.coords_to_point(time_line + rec_width/2, height + rec_height/2))
            recs.append(rec)
            animations.append(Write(rec))

            rec_uti_width, rec_uti_height = (task[0]/task[1]*uti_width), 1
            rec_uti = self.create_coords_rec(rec_uti_width, rec_uti_height, color)
            self.bring_to_back(rec_uti)
            rec_uti.move_to(self.coords_to_point(x_uti + rec_uti_width/2, uti_height + rec_uti_height/2))
            recs_uti.append(rec_uti)
            animations.append(Write(rec_uti))

            vec_release = self.create_coords_vec(0, 1, "#0000ff")
            vec_release.shift(self.coords_to_point(0, height))

            vec_deadline = self.create_coords_vec(0, -1, "#ff0000")
            vec_deadline.shift(self.coords_to_point(task[1], height + 1))
            vecs_deadline.append(vec_deadline)
            animations.append(ShowCreation(VGroup(vec_deadline, vec_release, line)))

            if first:
                first = False
                for i in range(0, 16, 5):
                    line = self.create_coords_line((i, 2), (i, 2 - .1))

                    text = TextMobject(f"{i}", color=COLOR_MAP["BLACK"])
                    text.move_to(self.coords_to_point(i, 2 - .5))
                    animations.append(ShowCreation(VGroup(text, line)))

            self.play(*animations)
            self.wait(1.5)

            height += 2
            time_line += task[0]
            x_uti += rec_uti_width

        self.wait(2)
        transforms = []

        new_vec_deadline = self.create_coords_vec(0, -1, "#ff0000")
        new_vec_deadline.shift(self.coords_to_point(12, 4 + 1))
        transforms.append(Transform(vecs_deadline[1], new_vec_deadline))

        # new_rec_width, new_rec_height = tasks[1][0], .7
        # new_rec = self.create_coords_rec(new_rec_width, new_rec_height, self.colors[1])
        # new_rec.move_to(self.coords_to_point(tasks[0][0] + tasks[1][0]/2, 4 + new_rec_height/2))
        # transforms.append(Transform(recs[1], new_rec))

        new_rec_uti = self.create_coords_rec(.5*uti_width, 1, self.colors[1])
        new_rec_uti.move_to(self.coords_to_point((.5 + .5/2)*uti_width + uti_offset, uti_height + 1/2))
        transforms.append(Transform(recs_uti[1], new_rec_uti))
        self.play(*transforms)
        self.wait(2)

        transforms = []
        new_deadlines = [10.9, 11.1]
        height = 2
        x_uti = uti_offset
        for new_deadline, rec_uti, vec_deadline, task, color in zip(new_deadlines, recs_uti, vecs_deadline, tasks,
                                                                    self.colors):
            new_vec_deadline = self.create_coords_vec(0, -1, "#ff0000")
            new_vec_deadline.shift(self.coords_to_point(new_deadline, height + 1))
            transforms.append(Transform(vec_deadline, new_vec_deadline))

            new_rec_uti_width, new_rec_uti_height = (task[0]/new_deadline)*uti_width, 1
            new_rec_uti = self.create_coords_rec(new_rec_uti_width, new_rec_uti_height, color)
            new_rec_uti.move_to(self.coords_to_point(x_uti + new_rec_uti_width/2, uti_height + new_rec_uti_height/2))
            transforms.append(Transform(rec_uti, new_rec_uti))
            x_uti += new_rec_uti_width
            height += 2

        self.play(*transforms)

        self.wait(5)

    def create_coords_rec(self, width: Num, height: Num, color: str = "#000000",
                          color_stroke: str = "#000000") -> Rectangle:
        point = self.coords_to_point(width, height)
        point -= self.coords_to_point(0, 0)
        rec = Rectangle(width=point[0], height=point[1], color=color)
        rec.set_stroke(color_stroke, opacity=1.)
        rec.set_fill(color, opacity=1.)
        return rec

    def create_coords_vec(self, x: Num, y: Num, color: str = "#000000") -> Vector:
        point = self.coords_to_point(x, y)
        point -= self.coords_to_point(0, 0)
        vec = Vector(point, color=color)
        return vec

    def create_coords_line(self, p_a: Coord, p_b: Coord, color: str = "#000000") -> Line:
        point_a, point_b = self.coords_to_point(*p_a), self.coords_to_point(*p_b)
        line = Line(point_a, point_b, color=color)
        return line

    def coords_to_point(self, x: float, y: float) -> np.ndarray:
        new_x = ((x - self.x_min)/(self.x_max - self.x_min))*self.x_axis_width - self.x_axis_width/2
        new_y = ((y - self.y_min)/(self.y_max - self.y_min))*self.y_axis_height - self.y_axis_height/2
        return np.array([new_x, new_y, 0])


if __name__ == "__main__":
    try:
        module_name = os.path.realpath(__file__)
        command = f"manim --leave_progress_bars -c white {' '.join(sys.argv[1:-1])} {module_name} {sys.argv[-1]}"
        print(f"Running: '{command}'")
        os.system(command)
    except KeyboardInterrupt:
        print("Stopping")
