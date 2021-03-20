from tkinter import Tk, Canvas, Frame, BOTH, ttk


class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="blue")
        self.grid()
        button = ttk.Button(self, text="Main menu", command=lambda: controller.show_frame("MainMenu"))
        button.grid()
