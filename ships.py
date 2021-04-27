
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
        another_lookup = {
            "Destroyer": "D",
            "Submarine": "S",
            "Cruiser": "C",
            "Battleship": "B",
            "Carrier": "A"
        }
        self.placement = []
        self.size = lookup[self.type]
        for x in range(0,self.size):
            self.placement.append(f"|{another_lookup[self.type]}")
        print(self.placement[::-1])
