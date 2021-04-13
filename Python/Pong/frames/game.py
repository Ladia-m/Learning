from tkinter import Tk, Canvas, Frame, BOTH, ttk, Entry
from time import sleep

from components import *


class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")
        buttons = self.create_buttons()
        buttons.pack(anchor="e")
        self.score_board = ScoreBoard(self)
        self.score_board.pack(anchor="center")
        self.play_field = PlayField(self)
        self.play_field.pack()
        self.left_paddle = Paddle(self.controller, self.play_field, "w", "s")
        self.right_paddle = Paddle(self.controller, self.play_field, "Up", "Down")
        self.ball = Ball(self, self.play_field)
        self.game_on = False
        self.game_over_label = None
        self.focus_set()

    def create_buttons(self):
        buttons = Frame(self, bg="black")
        button_style = ttk.Style()
        button_style.configure("W.TButton", font=("calibri", 10, "bold"), background="black", foreground="white")
        exit_button = ttk.Button(buttons, text="main menu", style="W.TButton", command=self.main_menu)
        exit_button.grid(row=0, column=2)
        restart_button = ttk.Button(buttons, text="restart game", style="W.TButton", command=self.restart)
        restart_button.grid(row=0, column=1)
        pause_button = ttk.Button(buttons, text="pause", style="W.TButton", command=self.pause)
        pause_button.grid(row=0, column=0)
        return buttons

    def start(self):
        self.game_on = True
        self.game_loop()

    def pause(self):
        if not self.game_over_label:
            self.game_on = False if self.game_on else True
            if self.game_on:
                self.game_loop()

    def reset(self):
        self.score_board.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.ball.reset()

    def restart(self):
        self.reset()
        if self.game_over_label:
            self.game_over_label.destroy()
            self.game_over_label = None
        self.game_on = True
        self.game_loop()

    def finish_game(self, winner):
        self.game_on = False
        self.game_over_label = ttk.Label(self, background="black", foreground="white", font="Verdana 30 bold",
                                         text=f"{winner} won!")
        self.game_over_label.place(x=230, y=300)

    def main_menu(self):
        self.game_on = False
        self.reset()
        self.controller.show_frame("MainMenu")

    def game_loop(self):
        while self.game_on:
            self.left_paddle.move()
            self.right_paddle.move()
            scored = self.ball.move()
            if scored:
                winner = self.score_board.update_score(scored)
                if winner:
                    self.finish_game(f"{winner} player")
                    break
                self.ball.reset()
                self.ball.wait(50)
            self.pong()
            self.controller.update()
            sleep(0.01)

    def pong(self):
        if (self.ball.x <= self.left_paddle.x_position + Paddle.width and
                self.ball.y + Ball.height >= self.left_paddle.y_position and
                self.ball.y <= self.left_paddle.y_position + Paddle.height):
            self.ball.bounce("x", self.pong_modificator_counter(self.ball.y, self.left_paddle.y_position))
        if (self.ball.x + self.ball.width >= self.right_paddle.x_position and
                self.ball.y + Ball.height >= self.right_paddle.y_position and
                self.ball.y <= self.right_paddle.y_position + Paddle.height):
            self.ball.bounce("x", self.pong_modificator_counter(self.ball.y, self.right_paddle.y_position))

    @staticmethod
    def pong_modificator_counter(ball_y, paddle_y):
        pong_position_pixels = ball_y - paddle_y + 20
        collision_range_pixels = Ball.height + Paddle.height
        pong_position_percentage = int(pong_position_pixels / collision_range_pixels * 100)
        return round((pong_position_percentage - 50) / 10)


