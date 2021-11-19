"""
COMP.CS.100
1.6.9 Rock/paper/scissors
Jani Ollenberg
H288244
"""


def main():
    player1 = input("Player 1, enter your choice (R/P/S): ")
    player2 = input("Player 2, enter your choice (R/P/S): ")
    if player1 == 'R':
        if player2 == 'R':
            winner = "tie"
        elif player2 == 'P':
            winner = 2
        elif player2 == 'S':
            winner = 1
    elif player1 == 'P':
        if player2 == 'R':
            winner = 1
        elif player2 == 'P':
            winner = 'tie'
        elif player2 == 'S':
            winner = 2
    elif player1 == 'S':
        if player2 == 'R':
            winner = 2
        elif player2 == 'P':
            winner=1
        elif player2 == 'S':
            winner = 'tie'

    if winner =='tie':
        print("It's a tie!")
    else:
        print(f'Player {winner} won!')


if __name__ == "__main__":
    main()