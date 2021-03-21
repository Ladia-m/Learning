from tkinter import Tk, Canvas, Frame, BOTH, ttk


class PlayField(Frame):

    def __init__(self, parent_frame):
        Frame.__init__(self, parent_frame)
        field = Canvas(self, width=800, height=500, bg="black")
        field.create_line(395, 0, 395, 500, fill="#ffffff", width=10)
        field.pack()


class Paddle:
    ...


class ScoreBorad(Frame):

    def __init__(self, parent_frame):
        Frame.__init__(self, parent_frame)
        left_player_score = 0
        right_player_score = 0
        max_score = 10
        left_score_label = ttk.Label(self, text=str(left_player_score)).grid(row=0, column=0)
        right_score_label = ttk.Label(self, text=str(right_player_score)).grid(row=0, column=2)
        double_dot_label = ttk.Label(self, text=":").grid(row=0, column=1)


    @staticmethod
    def setup(parent_frame):
        scoreboard = Canvas(parent_frame)


class Ball:
    ...
