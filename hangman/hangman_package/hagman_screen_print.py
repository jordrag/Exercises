# *********************************** Printing info on the screen  ********************************************
class ScreenPrint(object):
    def __init__(self, value):
        self.value = value

    def empty_word(self):
        print()
        for i in self.value:
            print(" _ ", end="")
        print()

    def in_game_print(self):
        print(" ".join(self.value))

    def hangman(self):
        print("It's wrong ! Hanging in progress...")
        print("*" * self.value)

    def guessed_letters(self):
        print(self.value)

    def win_result(self, hil_points, game_points):
        print(f"{self.value}, you won !")
        print(f"Total earned game points: {game_points}")
        print(f"Total HIL points: {hil_points}")

    def lost_result(self, hil_points, word, game_points):
        print(f"Game over! {self.value}, you've lost !")
        print(f"The word is -> {word}")
        print(f"Total earned game points: {game_points}")
        print(f"Total HIL points: {hil_points}")

    def change_params(self,points):
        print ("Leaving...")
        print(f"Total HIL points: {points}")


# ********************************************************************************************************
