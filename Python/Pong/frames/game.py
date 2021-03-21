from tkinter import Tk, Canvas, Frame, BOTH, ttk
from components import *


class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")
        score_board = ScoreBorad(self).grid(row=0, column=0)
        button = ttk.Button(self, text="Main menu", command=lambda: controller.show_frame("MainMenu"))
        button.grid(row=0, column=1)
        play_field_frame = PlayField(self).grid(row=1)

    def ui(self):
        ui_frame = Frame(self)
