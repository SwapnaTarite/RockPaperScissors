'''Modify the game so that the first player (or computer) to win two out of three
rounds is declared the overall winner. This adds a competitive aspect to the
game. '''

import random
arr=['r','p','s']
i=1
userwinrate=0
computerwinrate=0
while i<=3:
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
        elif(Choose=="r" and Computer=="s"):
                print("You Won")
                userwinrate=userwinrate+1
        elif(Choose=="r" and Computer=="p"):
                print("You Lost")
                computerwinrate= computerwinrate+1
        elif(Choose=="s" and Computer=="r"):
                print("You Lost")
                computerwinrate= computerwinrate+1
        elif(Choose=="s" and Computer=="p"):
                print("You Won")
                userwinrate=userwinrate+1
        elif(Choose=="p" and Computer=="r"):
                print("You Won")
                userwinrate=userwinrate+1
        elif(Choose=="p" and Computer=="s"):
                print("You Lost")
                computerwinrate= computerwinrate+1
        i=i+1
if userwinrate<computerwinrate:
        print("Computer  is the overall winner")
elif userwinrate>computerwinrate:
        print("You are the overall winner")
else:
        print("Tie")


