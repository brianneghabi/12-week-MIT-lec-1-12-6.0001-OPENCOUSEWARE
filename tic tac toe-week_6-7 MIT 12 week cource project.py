board = [" "] * 9

def show():
    print(f"\n{board[0] if board[0] != ' ' else '1'} | {board[1] if board[1] != ' ' else '2'} | {board[2] if board[2] != ' ' else '3'}")
    print("--+---+--")
    print(f"{board[3] if board[3] != ' ' else '4'} | {board[4] if board[4] != ' ' else '5'} | {board[5] if board[5] != ' ' else '6'}")
    print("--+---+--")
    print(f"{board[6] if board[6] != ' ' else '7'} | {board[7] if board[7] != ' ' else '8'} | {board[8] if board[8] != ' ' else '9'}")


wins = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]


while True:

    # Reset the board for a new game
    board = [" "] * 9

    turn = 0

    while turn < 9:
        show()

        player = "X" if turn % 2 == 0 else "O"

        # Keep asking until the player makes a valid move
        while True:
            try:
                move = int(input(f"Player {player}, choose 1-9: ")) - 1

                if move < 0 or move > 8:
                    print("Please choose a number from 1-9!")
                    continue

                if board[move] != " ":
                    print("That spot is taken!")
                    continue

                # Valid move
                break

            except ValueError:
                print("Please enter a number from 1-9!")

        board[move] = player
        turn += 1

        # Check for winner
        if any(board[a] == board[b] == board[c] != " " for a, b, c in wins):
            show()
            print(f"Player {player} wins! 🎉")
            break

    else:
        show()
        print("It's a draw!")

    # Ask if they want to play again
    while True:
        again = input("Play again? (yes/no): ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("Thanks for playing!")
            exit()
        else:
            print("Please enter yes or no.")