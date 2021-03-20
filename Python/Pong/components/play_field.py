import sys
from tkinter import Tk, Canvas, Frame, BOTH, ttk


class PlayField:

    def exit(self):
        sys.exit(0)

    def setup(self, frame):

        root = Tk()

        root.title("Pong")
        root.geometry("800x600")
        root.config(bg="black")


    def middle_line(self, root_window):
        ...

