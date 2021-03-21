#!/usr/bin/env python3

from frames.main_menu import MainMenu
from frames.game import Game
from tkinter import Tk, Frame


class Pong(Tk):
    active_frame = "MainMenu"

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Pong")
        self.geometry("810x600")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, Game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            # frame.grid(row=0, column=0, sticky="nsew")
        self.frames["MainMenu"].grid()

    def show_frame(self, page_name):
        frame = self.frames[self.active_frame]
        frame.grid_forget()
        frame = self.frames[page_name]
        frame.grid(sticky="nsew")
        self.active_frame = page_name


if __name__ == "__main__":
    Pong().mainloop()
