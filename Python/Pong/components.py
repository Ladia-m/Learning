from tkinter import Canvas, Frame, ttk


class ScoreBoard(Frame):
    max_score = 10

    def __init__(self, parent_frame):
        Frame.__init__(self, parent_frame)
        self.left_player_score = 0
        self.right_player_score = 0
        self.left_score_label = ttk.Label(self, text=str(self.left_player_score))
        self.left_score_label.grid(row=0, column=0)
        self.right_score_label = ttk.Label(self, text=str(self.right_player_score))
        self.right_score_label.grid(row=0, column=2)
        double_dot_label = ttk.Label(self, text=":")
        double_dot_label.grid(row=0, column=1)
        for label in (self.left_score_label, self.right_score_label, double_dot_label):
            label.config(background="black", foreground="white", font="Verdana 30 bold")

    def update_score(self, player: str):
        if player == "left":
            self.left_player_score += 1
            self.left_score_label.config(text=str(self.left_player_score))
            if self.left_player_score == ScoreBoard.max_score:
                return "left"
        if player == "right":
            self.right_player_score += 1
            self.right_score_label.config(text=str(self.right_player_score))
            if self.right_player_score == ScoreBoard.max_score:
                return "right"
        return False


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
    x_padding = 5
    width = 12
    height = 80
    speed = 4

    def __init__(self, controller, play_field: Canvas, up_key, down_key):
        super().__init__(play_field, width=self.width, height=self.height, bg="white")
        if Paddle.paddle_objects_created > 1:
            raise SystemError("Can't create more than 2 Paddle objects")
        Paddle.paddle_objects_created += 1
        self.x_position = self.x_padding if Paddle.paddle_objects_created == 1 else PlayField.width - self.x_padding - self.width
        self.y_position = PlayField.height // 2 - self.height // 2
        self.place(x=self.x_position, y=self.y_position)
        self.controller, self.up_key, self.down_key = controller, up_key, down_key
        self.controller.bind(f"<{up_key}>", self.move_up_repeat)
        self.controller.bind(f"<KeyRelease-{up_key}>", self.stop_move_up_repeat)
        self.controller.bind(f"<{down_key}>", self.move_down_repeat)
        self.controller.bind(f"<KeyRelease-{down_key}>", self.stop_move_down_repeat)
        self.move_up_key = False
        self.move_down_key = False

    def move_up_repeat(self, event):
        self.move_up_key = True

    def stop_move_up_repeat(self, event):
        self.move_up_key = False

    def move_down_repeat(self, event):
        self.move_down_key = True

    def stop_move_down_repeat(self, event):
        self.move_down_key = False

    def move(self):
        if self.move_up_key:
            self.y_position -= self.speed
        if self.move_down_key:
            self.y_position += self.speed
        if 0 < self.y_position < PlayField.height - Paddle.height:
            self.place(y=self.y_position)


class Ball(Canvas):
    width = 20
    height = 20
    speed = 4

    def __init__(self, root, play_field: Canvas):
        super().__init__(play_field, width=self.width, height=self.height, bg="white")
        self.x, self.y = PlayField.width / 2 - self.width / 2, PlayField.height / 2 - self.height / 2
        self.place(x=self.x, y=self.y)
        self.starting_side = 1
        self.x_speed = self.speed * self.starting_side
        self.y_speed = 0
        self.wait_counter = 0

    def move(self):
        if self.wait_counter != 0:
            self.wait_counter -= 1
            return
        if self.y >= PlayField.height - self.height or self.y < 1:
            self.bounce("y")
        self.x += self.x_speed
        self.y += self.y_speed
        self.place(x=self.x, y=self.y)
        if self.x > PlayField.width - self.width:
            return "left"
        if self.x <= 0:
            return "right"

    def wait(self, loops: int):
        self.wait_counter = loops

    def bounce(self, plane, y_speed=0):
        if plane == "x":
            self.x_speed = self.x_speed * -1
            self.y_speed = y_speed
        if plane == "y":
            self.y_speed = self.y_speed * -1

    def reset(self):
        self.starting_side = self.starting_side * -1
        self.x_speed = self.speed * self.starting_side
        self.y_speed = 0
        self.x, self.y = PlayField.width / 2 - self.width / 2, PlayField.height / 2 - self.height / 2
        self.place(x=self.x, y=self.y)
