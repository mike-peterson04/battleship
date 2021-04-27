from board import Board
from ships import Ship

class Player():
    def __init__(self):
        self.name = ''
        self.board = Board()
        self.ships = [Ship("Destroyer"), Ship("Submarine"), Ship("Cruiser"), Ship("Battleship"), Ship("Carrier")]

    def setup_board(self):
        for x in self.ships:
            self.board.place_ship(x)