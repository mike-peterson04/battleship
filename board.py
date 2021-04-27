


class Board:
    def __init__(self):

        self.field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        x = 0
        while x < 20:
            self.field[x] = ["|_", "|_", "|_", "|_", "|_", "|_", "|_", "|_", "|_", "|_", "|_", "|_", "|_",
                             "|_", "|_", "|_", "|_", "|_", "|_", "|_"]
            x += 1

    def place_ship(self, ship):
        index = {
            'A' : 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
        }
        self.player_view()
        print("do you want to place your ship horizontally or vertically?")
        print("1:Horizontally")
        print("2:Vertically")
        check = int(input())
        coordinates = ["",""]
        print("What row do you want your bow placed on? pick 1-20")
        coordinates[1] = int(input())
        print("What column do you want your bow placed on? pick A-T")
        coordinates[0] = index[input().upper()]
        for x in ship.placement:
            if check == 1:
                self.field[coordinates[0]][coordinates[1]-1] = x
                coordinates[0] += 1
            else:
                self.field[coordinates[0]][coordinates[1]-1] = x
                coordinates[1] += 1
        self.player_view()



    def opponent_view(self):
        pass

    def player_view(self):
        print("__|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|")
        i = 0
        while i < 20:
            row = ''
            if i < 9:
                row = '0'
            row += f"{i+1}"
            for x in self.field:
                row += x[i]
            print(row+"|")
            i += 1
