#This program is a player vs. computer Tic-Tac-Toe game
from enum import Enum
import random

class GridSquare():
    state = ""
    pos = 0

    def __init__(self, x):
        self.pos = x
        self.state = "-1"

    def draw_space(self):
        if self.state == "1":
            return 'X'
        if self.state == "0":
            return 'O'
        return str(self.pos)[0]

class TicTacToe():
    cols = 3
    rows = 3
    total_turns = 0
    winner = -1
    
    
    class game_state(Enum):
        OVER = 0
        RUNNING = 1

    current_state = game_state.OVER
    board = None
    
    
    def setup(self):
        self.board = [[None] * self.cols for _ in range(self.rows)]
        position = 1
        r = 0
        while r < self.rows:
            c = 0
            while c < self.cols:
                self.board[r][c] = GridSquare(position)
                position += 1
                c += 1
            r += 1
        TicTacToe.current_state = TicTacToe.game_state.RUNNING
        self.play_game()
       
    def play_game(self):
        while TicTacToe.current_state == TicTacToe.game_state.RUNNING:
            self.display_board()
            self.make_move()
        if TicTacToe.current_state == TicTacToe.game_state.OVER:
                self.display_game_over()

    def display_board(self):
        print("\n"+" "+str(self.board[0][0].draw_space())+" | "+str(self.board[0][1].draw_space())+" | "+str(self.board[0][2].draw_space()))
        print("___|___|___")
        print("\n"+" "+str(self.board[1][0].draw_space())+" | "+str(self.board[1][1].draw_space())+" | "+str(self.board[1][2].draw_space()))
        print("___|___|___")
        print("\n"+" "+str(self.board[2][0].draw_space())+" | "+str(self.board[2][1].draw_space())+" | "+str(self.board[2][2].draw_space()))
        print("   |   |   ")

    def make_move(self):
        if str(self.get_player()) == "X":
            ai = random.randint(1, 9)
            print("PlayerXchose" + str(ai))
            i = 0
            while i < self.cols:
                j = 0
                while j < self.rows:
                    if str(self.board[i][j].state) == "-1" and str(self.board[i][j].pos) == str(ai):
                        self.board[i][j].state = str(self.total_turns % 2)
                        self.total_turns += 1
                        self.check_win(i,j,str(self.board[i][j].state))
                    j += 1
                i += 1

        if str(self.get_player()) == "O": 
            print("Player " + str(self.get_player()) + " choose a pos: ")
            spot = input()
            i = 0
            while i < self.cols:
                j = 0
                while j < self.rows:
                    if str(self.board[i][j].state) == "-1" and str(self.board[i][j].pos) == spot:
                        self.board[i][j].state = str(self.total_turns % 2)
                        self.total_turns += 1
                        self.check_win(i,j,str(self.board[i][j].state))
                    j += 1
                i += 1


    def display_game_over(self):
        self.display_board()
        print("Game Over!")
        if self.winner == "1":
            print("X Wins")
        if self.winner == "0":
            print("O Wins")
        if self.total_turns == 9 and not (self.winner == "1") and not self.winner == "0":
            print("Tie!")


    def get_player(self):
        if self.total_turns%2 == 0:
            return 'O'
        return 'X'

    def check_win(self, x, y, turn):
        col_win = 0
        row_win = 0
        diag1_win = 0
        diag2_win = 0
        i = 0

        while i < 3:
            if self.board[x][i].state == turn:
                 col_win += 1
            if self.board[i][y].state == turn:
                 row_win += 1
            if self.board[i][i].state == turn:
                 diag1_win += 1
            if self.board[i][2 - i].state == turn:
                 diag2_win += 1
            i += 1
        if col_win == 3 or row_win == 3 or diag1_win ==3 or diag2_win ==3:
            self.winner = turn
            if self.winner != -1:
                TicTacToe.current_state = TicTacToe.game_state.OVER
        if self.total_turns == 9:
            TicTacToe.current_state = TicTacToe.game_state.OVER

game_play = TicTacToe()
game_play.setup()

