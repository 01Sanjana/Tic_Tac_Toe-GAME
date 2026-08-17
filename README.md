# Tic_Tac_Toe-GAME
# It is the task code CODE-ALFA internship
'''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9   '''


# numbers = ["X", "O", "3", "4", "X", "6", "O", "8", "X"]
numbers=[]
for i in range(1,10):
    numbers.append(i)


for i in range(0,9,3):
    print(f"{numbers[i]} | {numbers[i+1]} | {numbers[i+2]}")
    print("----------")

i=0
while(i<3):
    user1=int(input("user1 ,Enter the position (1-9) :"))
    user2=int(input("user2 ,Enter the position (1-9) :"))
    i+=1

    numbers[user1-1]='X'
    if user1==user2:
        print("Invalid !")
    else:
        numbers[user2-1]='O'

    print("\nAFTER\n")
    print(numbers)
    for num in range(0,9,3):
        print(f"{numbers[num]} | {numbers[num+1]} | {numbers[num+2]}")
        print("----------")
