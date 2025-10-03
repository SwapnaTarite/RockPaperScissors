'''Keep a tally of how many times the player wins, loses, or ties with the
computer. Display these statistics at the end of the game.'''

import random
arr=['r','p','s']
winrate=0
lossrate=0
tierate=0
while True:
        Choose=input("Rock , Paper  or Scissors  ? (r,p,s) :")
        Computer=random.choice(arr)
        if Choose=='r':
            print("You choose \U0001FAA8")
        elif Choose=='p':
            print("You choose \U0001F4C4")
        elif Choose=='s':
            print("You choose \u2702\ufe0f")
        else:
            print("Choose the correct option")
        if Computer=='r':
            print("Computer choose \U0001FAA8")
        elif Computer=='p':
            print("Computer choose \U0001F4C4")
        elif Computer=='s':
            print("Computer choose \u2702\ufe0f")
        if (Choose=='r' and Computer=='r') or (Choose=='r' and Computer=='r') or (Choose=='r' and Computer=='r'):
            print("Its a tie")
            tierate=tierate+1
        elif(Choose=="r" and Computer=="s"):
                print("You Won")
                winrate=winrate+1
        elif(Choose=="r" and Computer=="p"):
                print("You Lost")
                lossrate=lossrate+1
        elif(Choose=="s" and Computer=="r"):
                print("You Lost")
                lossrate=lossrate+1
        elif(Choose=="s" and Computer=="p"):
                print("You Won")
                winrate=winrate+1
        elif(Choose=="p" and Computer=="r"):
                print("You Won")
                winrate=winrate+1
        elif(Choose=="p" and Computer=="s"):
                print("You Lost")
                lossrate=lossrate+1
        val=input("Do you want to continue ?(y/n) :").lower()
        if val=='n':
            print(f"wins : {winrate} \nlosses  : {lossrate}\nties : {tierate}")
            break


