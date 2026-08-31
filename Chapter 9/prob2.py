import random

def game():
    print("You are playing a game: ")
    score = random.randint(1, 100)
    #Fetch the hiscore from the file
    with open("hiscore.txt") as f:
        