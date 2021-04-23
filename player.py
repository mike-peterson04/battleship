from board import Board
from ships import Ship

class Player():
    def __init__(self):
        self.board = Board()
        self.ships = [Ship("Destroyer"), Ship("Submarine"), Ship("Cruiser"), Ship("Battleship"), Ship("Carrier")]