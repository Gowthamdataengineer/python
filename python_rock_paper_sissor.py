import random

while True:
    player=input("Rock,Paper,Scissors? : ")
    computer =  random.choice(['Rock','Paper','Scissors'])

    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!",computer,"covers",player)
        else:
            print("You win ! ", player,"Smashes",computer)

    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!",computer,"cut",player)
        else:
            print("You win ! ", player,"covers",computer)

    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!",computer,"Smashes",player)
        else:
            print("You win ! ", player,"cut",computer)

    else:
        print("check your spelling !!")
