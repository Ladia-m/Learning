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
        paddle_1 = Paddle(play_field)
        paddle_2 = Paddle(play_field)

    def ui(self):
        ui_frame = Frame(self, width=800, height=100)
        button = ttk.Button(ui_frame, text="Main menu", style="W.TButton", command=lambda: self.controller.show_frame("MainMenu"))
        button.pack(anchor="e")
        score_board = ScoreBorad(ui_frame)
        score_board.pack(anchor="center")
        return ui_frame
