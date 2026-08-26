computer = -1
youstr = input("Enter Your Choice: ")
Dict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

you = Dict[youstr]

if (computer == -1 and you == 1):
    print("You win")
elif(computer == -1 and you == 0):
    print("You lose")
elif(computer == 1 and you == -1):
    print("You lose")
elif(computer == 1 and you == 0):
    print("You win")
elif(computer == 0 and you == -1):
    print("You win")
elif(computer == 0 and you == 1):
    print("You lose")
else:
    print("Somthing went wrong! \nPlease try again...")


'''
1 for  snake
-1 for water
0 for gun

'''