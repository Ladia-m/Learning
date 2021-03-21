import sys
from tkinter import Tk, Canvas, Frame, BOTH, ttk


class MainMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black", width=800, height=600)
        self.game_logo(self).grid(row=0)
        self.menu(controller).grid(row=1)

    @staticmethod
    def game_logo(parent):
        logo_frame = Frame(parent)
        ttk.Label(logo_frame, text="Pong!").pack()
        return logo_frame

    def menu(self, controller):
        menu_frame = Frame(self)
        buttons = {
            "start_game": ttk.Button(menu_frame, text="Start game", command=lambda: controller.show_frame("Game")),
            "exit_game": ttk.Button(menu_frame, text="Exit game", command=lambda: sys.exit(0))
        }
        counter = 0
        for button in buttons.keys():
            buttons[button].grid(row=counter, pady=5)
            counter += 1
        return menu_frame
