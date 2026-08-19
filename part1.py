'''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''


numbers = []


# Display the board
def display_board():
    for i in range(0, 9, 3):
        print(f"{numbers[i]} | {numbers[i+1]} | {numbers[i+2]}")
        print("----------")


# Check winning combinations
def check_winner():
    c1 = numbers[0] == numbers[1] == numbers[2]
    c2 = numbers[3] == numbers[4] == numbers[5]
    c3 = numbers[6] == numbers[7] == numbers[8]

    c4 = numbers[0] == numbers[3] == numbers[6]
    c5 = numbers[1] == numbers[4] == numbers[7]
    c6 = numbers[2] == numbers[5] == numbers[8]

    c7 = numbers[0] == numbers[4] == numbers[8]
    c8 = numbers[2] == numbers[4] == numbers[6]

    if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8:
        return True

    return False


# Start the game
def play_game():

    global numbers

    numbers = []

    # Create the board
    for i in range(1, 10):
        numbers.append(i)

    print()
    display_board()

    player = "X"
    turn = 0

    # Take turns
    while turn < 9:

        try:
            position = int(
                input(f"Player {player}, enter the position (1-9): ")
            )

            # Check if position is between 1 and 9
            if position < 1 or position > 9:
                print("Invalid position! Please enter a number from 1 to 9.")
                continue

            # Check if position is available
            if numbers[position - 1] != "X" and numbers[position - 1] != "O":

                numbers[position - 1] = player

                # Count only valid moves
                turn += 1

                print()
                display_board()

                # Check for winner
                if check_winner():
                    print(f"Player {player} wins!")
                    return

                # Switch player
                if player == "X":
                    player = "O"
                else:
                    player = "X"

            else:
                print("Position already occupied!")

        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")

    # If all 9 valid moves are completed without a winner
    print("It is a Tie/Draw!")


# Play the game
while True:

    play_game()

    choice = input("Do you want to play again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thanks for playing!")
        break