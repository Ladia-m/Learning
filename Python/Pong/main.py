#!/usr/bin/env python3

from frames.main_menu import MainMenu
from frames.game import Game
from tkinter import Tk, Frame


class Pong(Tk):
    active_frame = "MainMenu"
    window_width = 810
    window_height = 600

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Pong")
        self.geometry(f"{self.window_width}x{self.window_height}")
        self.resizable(0, 0)
        container = Frame(self, bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.center()

        self.frames = {}
        for F in (MainMenu, Game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
        self.frames["MainMenu"].grid()

    def show_frame(self, page_name):
        frame = self.frames[self.active_frame]
        frame.grid_forget()
        frame = self.frames[page_name]
        frame.grid()
        self.active_frame = page_name

    def center(self):
        positionRight = int(self.winfo_screenwidth() / 2 - self.window_width / 2)
        positionDown = int(self.winfo_screenheight() / 2 - self.window_height / 2)
        self.geometry("+{}+{}".format(positionRight, positionDown))


if __name__ == "__main__":
    Pong().mainloop()
