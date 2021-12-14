"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for Mölkky.
Jani Ollenberg
H288244
"""


# TODO:
# a) Implement the class Player here.
class Player():
    """
    Player class keeps track of player's score.
    """

    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__throws = []

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def has_won(self):
        return self.__points == 50

    def add_points(self, points):
        self.__throws.append(points)
        self.__points += points
        if self.__points > 50:
            self.__points = 25
            print(f"{self.__name} gets penalty points!")
        if self.__points >= 40 and self.__points < 50:
            needed_points = 50 - self.__points
            print(f"{self.__name} needs only {needed_points} points. It's \
better to avoid knocking down the pins with higher points.")

    def throw_average(self):
        sum = 0
        for throw in self.__throws:
            sum += throw 
        return sum / len(self.__throws)
    
    def hit_percentage(self):
        hits = 0
        if len(self.__throws) == 0:
            return 0
        for throw in self.__throws:
            if throw > 0:
                hits += 1
        return hits / len(self.__throws) * 100

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        if pts > in_turn.throw_average():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, \
hit percentage {player1.hit_percentage():.1f}")  # TODO: d)
        print(f"{player2.get_name()}: {player2.get_points()} p, \
hit percentage {player2.hit_percentage():.1f}")  # TODO: d)
        # print(player2.get_name() + ":", player2.get_points(), "p")  # TODO: d)
        print("")

        throw += 1


if __name__ == "__main__":
    main()
