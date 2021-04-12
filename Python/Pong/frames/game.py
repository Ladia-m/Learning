from tkinter import Tk, Canvas, Frame, BOTH, ttk, Entry
from time import sleep

from components import *


class Game(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="black")
        self.score_board = None
        # TODO: change ui directly into scoreboard without subframe
        ui_frame = self.ui()
        ui_frame.config(bg="black")
        ui_frame.grid(row=0, sticky="we")
        button_style = ttk.Style()
        button_style.configure("W.TButton", font=("calibri", 10, "bold"), background="black", foreground="white")

        play_field = PlayField(self)
        play_field.grid(row=1)
        self.left_paddle = Paddle(self.controller, play_field, "Up", "Down")
        self.right_paddle = Paddle(self.controller, play_field, "w", "s")
        self.ball = Ball(self, play_field)
        self.game_on = False
        self.focus_set()

    def ui(self):
        ui_frame = Frame(self, width=800, height=100)
        button = ttk.Button(ui_frame, text="Main menu", style="W.TButton",
                            command=self.exit_game)
        button.pack(anchor="e")
        self.score_board = ScoreBoard(ui_frame)
        self.score_board.pack(anchor="center")
        return ui_frame

    def start_game(self):
        self.game_on = True
        self.game_loop()

    def exit_game(self):
        self.game_on = False
        self.controller.show_frame("MainMenu")

    def finish_game(self, winner):
        self.game_on = False

    def game_loop(self):
        while self.game_on:
            self.left_paddle.move()
            self.right_paddle.move()
            scored = self.ball.move()
            if scored:
                winner = self.score_board.update_score(scored)
                if winner:
                    self.finish_game(winner)
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


