'''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9   '''


numbers = []

# Create the board
for i in range(1, 10):
    numbers.append(i)

for i in range(0, 9, 3):
    print(f"{numbers[i]} | {numbers[i+1]} | {numbers[i+2]}")
    print("----------")

player = "X"

# Take turns
for turn in range(9):

    # Take input
    position = int(input(f"Player {player}, enter the position (1-9): "))

    # Check if position is available
    if numbers[position - 1] != "X" and numbers[position - 1] != "O":
        numbers[position - 1] = player

        # Display updated board
        print()

        for i in range(0, 9, 3):
            print(f"{numbers[i]} | {numbers[i+1]} | {numbers[i+2]}")
            print("----------")

        # Check winning combinations
        c1 = numbers[0] == numbers[1] == numbers[2]
        c2 = numbers[3] == numbers[4] == numbers[5]
        c3 = numbers[6] == numbers[7] == numbers[8]

        c4 = numbers[0] == numbers[3] == numbers[6]
        c5 = numbers[1] == numbers[4] == numbers[7]
        c6 = numbers[2] == numbers[5] == numbers[8]

        c7 = numbers[0] == numbers[4] == numbers[8]
        c8 = numbers[2] == numbers[4] == numbers[6]

        if c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8:
            print(f"Player {player} wins!")
            break

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        print("Position already occupied!")