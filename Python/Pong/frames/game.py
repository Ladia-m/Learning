from tkinter import Tk, Canvas, Frame, BOTH, ttk, Entry
from components import *


class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")
        ui_frame = self.ui()
        ui_frame.config(bg="black")
        ui_frame.grid(row=0, sticky="we")
        button_style = ttk.Style()
        button_style.configure("W.TButton", font=("calibri", 10, "bold"), background="black", foreground="white")

        play_field = PlayField(self)
        play_field.grid(row=1)
        self.paddle_1 = Paddle(self.controller, play_field, "Up", "Down")
        self.paddle_2 = Paddle(self.controller, play_field, "w", "s")
        self.ball = Ball(self, play_field)

        self.focus_set()

    def ui(self):
        ui_frame = Frame(self, width=800, height=100)
        button = ttk.Button(ui_frame, text="Main menu", style="W.TButton",
                            command=lambda: self.controller.show_frame("MainMenu"))
        button.pack(anchor="e")
        score_board = ScoreBoard(ui_frame)
        score_board.pack(anchor="center")
        return ui_frame
