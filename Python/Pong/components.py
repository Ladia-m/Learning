from tkinter import Tk, Canvas, Frame, BOTH, ttk, font


class PlayField(Frame):

    def __init__(self, parent_frame):
        Frame.__init__(self, parent_frame)
        field = Canvas(self, width=800, height=500, bg="black")
        field.create_line(397, 0, 397, 500, fill="#ffffff", dash=(20, 10), width=6)
        field.pack()


class Paddle:
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

    @staticmethod
    def setup(parent_frame):
        scoreboard = Canvas(parent_frame)


class Ball:
    ...
