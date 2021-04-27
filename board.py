


class Board:
    def __init__(self):

        self.field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        x = 0
        while x < 20:
            self.field[x] = ["|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|",
                             "|_|", "|_|", "|_|", "|_|", "|_|", "|_|", "|_|"]
            x += 1

    def place_ship(self, ship):
        self.player_view()
        print("do you want to place your ship horizontally or vertically?")
        print("1:Horizontally")
        print("2:Vertically")
        check = int(input())
        print("What row")


    def opponent_view(self):
        pass

    def player_view(self):
        print("A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|")
        i = 0
        while i < 20:
            row = f"{i+1}"
            for x in self.field:
                row += x[i]
            i += 1
