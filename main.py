from game import Game


def test_method():
    battleship = Game()
    battleship.player_one.board.place_ship(battleship.player_one.ships[4])
    battleship.player_one.board.player_view()


if __name__ == '__main__':
    test_method()

