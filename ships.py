
class Ship():
    def __init__(self, type):
        self.type = type
        lookup = {
            "Destroyer": 2,
            "Submarine": 3,
            "Cruiser": 3,
            "Battleship": 4,
            "Carrier": 5
        }
        self.size = lookup[self.type]
