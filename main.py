from game import Game


# def test_method():
#     battleship = Game()

if __name__ == '__main__':
    # test_method()

    alphabet = ["A","B","C","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    count=0
    print("_|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|")
    while count < 20:
        carrier = "__"
        if count > 5 and count < 11:
            carrier = "_a"
            if count > 9 and count < 11:
                carrier = "_A"
        print(f"{alphabet[count]}|__|__|__|__|__|__|__|__|__|__|__|{carrier}|__|__|__|__|__|__|__|__|")
        count = count + 1