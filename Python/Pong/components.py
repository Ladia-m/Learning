from tkinter import Tk, Canvas, Frame, BOTH, ttk, font
from time import sleep


class PlayField(Canvas):
    width = 800
    height = 500

    def __init__(self, parent_frame):
        Canvas.__init__(self, parent_frame, width=self.width, height=self.height, bg="black")
        self.create_line(self.width / 2, 0, self.width / 2, 500, fill="#ffffff", dash=(20, 10), width=6)
        self.create_line(1, 1, 800, 1, fill="#ffffff", width=1)
        self.create_line(800, 1, 800, 500, fill="#ffffff", width=1)
        self.create_line(800, 500, 1, 500, fill="#ffffff", width=1)
        self.create_line(1, 500, 1, 1, fill="#ffffff", width=1)


class Paddle(Canvas):
    paddle_objects_created = 0
    x_padding = 10
    width = 12
    height = 80
    speed = 5

    def __init__(self, controller, play_field: Canvas, up_key, down_key):
        super().__init__(play_field, width=self.width, height=self.height, bg="white")
        if Paddle.paddle_objects_created > 1:
            raise SystemError("Can't create more than 2 Paddle objects")
        Paddle.paddle_objects_created += 1
        x = self.x_padding if Paddle.paddle_objects_created == 1 else PlayField.width - self.x_padding - self.width
        self.y_position = PlayField.height // 2 - self.height // 2
        self.place(x=x, y=self.y_position)
        self.controller, self.up_key, self.down_key = controller, up_key, down_key
        self.controller.bind(f"<{up_key}>", self.move_up_repeat)
        self.controller.bind(f"<KeyRelease-{up_key}>", self.stop_move_up_repeat)
        self.controller.bind(f"<{down_key}>", self.move_down_repeat)
        self.controller.bind(f"<KeyRelease-{down_key}>", self.stop_move_down_repeat)
        self.up_released = True
        self.down_released = True

    def move_up_repeat(self, event):
        self.up_released = False
        while not self.up_released:
            self.move_up()
            sleep(0.02)
            self.controller.update()

    def move_up(self):
        self.y_position -= self.speed
        self.place(y=self.y_position)

    def stop_move_up_repeat(self, event):
        self.up_released = True

    def move_down_repeat(self, event):
        self.down_released = False
        while not self.down_released:
            self.move_down()
            sleep(0.02)
            self.controller.update()

    def move_down(self):
        self.y_position += self.speed
        self.place(y=self.y_position)

    def stop_move_down_repeat(self, event):
        self.down_released = True


class ScoreBoard(Frame):

    def __init__(self, parent_frame):
        Frame.__init__(self, parent_frame)
        left_player_score = 0
        right_player_score = 0
        max_score = 10
        left_score_label = ttk.Label(self, text=str(left_player_score))
        left_score_label.grid(row=0, column=0)
        right_score_label = ttk.Label(self, text=str(right_player_score))
        right_score_label.grid(row=0, column=2)
        double_dot_label = ttk.Label(self, text=":")
        double_dot_label.grid(row=0, column=1)
        for label in (left_score_label, right_score_label, double_dot_label):
            label.config(background="black", foreground="white", font="Verdana 30 bold")


class Ball(Canvas):
    width = 20
    height = 20

    def __init__(self, root, play_field: Canvas):
        super().__init__(play_field, width=self.width, height=self.height, bg="white")
        self.x, self.y = PlayField.width / 2 - self.width / 2, PlayField.height / 2 - self.height / 2
        self.place(x=self.x, y=self.y)
        self.starting_side = 1
        self.x_speed = 10 * self.starting_side
        self.y_speed = 0

    def move(self):
        if self.y >= PlayField.height - self.height:
            self.bounce("y")
        self.x += self.x_speed
        self.y += self.y_speed
        self.place(x=self.x, y=self.y)
        if self.x > PlayField.width - self.width:
            return "left scored"
        if self.x < PlayField.width:
            return "right scored"

    def bounce(self, plane, y_speed_change=0):
        if plane == "x":
            self.x_speed = self.x_speed * -1
        self.y_speed += y_speed_change
        if self.y_speed > 10:
            self.y_speed = 10
        if plane == "y":
            self.y_speed = self.y_speed * -1

    def reset(self):
        self.starting_side = self.starting_side * -1
        self.x_speed = 10 * self.starting_side
        self.y_speed = 0
        self.x, self.y = PlayField.width / 2 - self.width / 2, PlayField.height / 2 - self.height / 2
        self.place(x=self.x, y=self.y)
