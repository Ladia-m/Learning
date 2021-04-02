from tkinter import Tk, Canvas, Frame, BOTH, ttk, font


class PlayField(Canvas):
    width = 800
    height = 500

    def __init__(self, parent_frame):
        Canvas.__init__(self, parent_frame, width=self.width, height=self.height, bg="black")
        self.create_line(397, 0, 397, 500, fill="#ffffff", dash=(20, 10), width=6)
        self.create_line(1, 1, 800, 1, fill="#ffffff", width=1)
        self.create_line(800, 1, 800, 500, fill="#ffffff", width=1)
        self.create_line(800, 500, 1, 500, fill="#ffffff", width=1)
        self.create_line(1, 500, 1, 1, fill="#ffffff", width=1)


class Paddle(Canvas):
    paddle_objects_created = 0
    x_padding = 10
    width = 12
    height = 80
    speed = 10

    def __init__(self, play_field: Canvas):
        super().__init__(play_field, width=self.width, height=self.height, bg="white")
        if Paddle.paddle_objects_created > 1:
            raise SystemError("Can't create more than 2 Paddle objects")
        Paddle.paddle_objects_created += 1
        x = self.x_padding if Paddle.paddle_objects_created == 1 else PlayField.width - self.x_padding - self.width
        self.y_position = PlayField.height // 2 - self.height // 2
        self.place(x=x, y=self.y_position)

    def move_up(self):
        self.y_position -= self.speed
        self.place(y=self.y_position)

    def move_down(self):
        lowest_position = PlayField.height - self.height
        ...


class ScoreBorad(Frame):

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


class Ball:
    ...
