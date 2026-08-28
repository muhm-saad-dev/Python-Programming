import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
Dict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

revDict = {
    1 : "Snak",
    -1 : "Water",
    0 : "Gun"
}

you = Dict[youstr]

print(f"Computer Chose {revDict[computer]} \nYou Chose {revDict[you]}")

if (computer == you):
    print("Its a Draw")
else:
    # if (computer == -1 and you == 1):
    #     print("You win")
    # elif(computer == -1 and you == 0):
    #     print("You lose")
    # elif(computer == 1 and you == -1):
    #     print("You lose")
    # elif(computer == 1 and you == 0):
    #     print("You win")
    # elif(computer == 0 and you == -1):
    #     print("You win")
    # elif(computer == 0 and you == 1):
    #     print("You lose")
    # else:
    #     print("Somthing went wrong! \nPlease try again...")


    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose")
    else:
        print("You win")



'''
1 for  snake
-1 for water
0 for gun

'''