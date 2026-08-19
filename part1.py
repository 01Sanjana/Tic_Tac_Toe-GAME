'''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9   '''


# numbers = ["X", "O", "3", "4", "X", "6", "O", "8", "X"]
numbers = []

# Create the board
for i in range(1, 10):
    numbers.append(i)


# Display the board
for i in range(0, 9, 3):
    print(f"{numbers[i]} | {numbers[i+1]} | {numbers[i+2]}")
    print("----------")


player = "X"

# Take turns
for turn in range(6):

    position = int(input(f"Player {player}, enter the position (1-9): "))

    numbers[position - 1] = player

    # Display updated board
    print()

    for i in range(0, 9, 3):
        print(f"{numbers[i]} | {numbers[i+1]} | {numbers[i+2]}")
        print("----------")

    # Switch player
    if player == "X":
        player = "O"
    else:
        player = "X"