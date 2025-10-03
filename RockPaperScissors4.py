'''Add an option for two players to play against each other, taking turns to input
their choices. The program should then determine the winner based on their
inputs.'''
while True:
        Player1=input("Player1 : Choose Rock , Paper  or Scissors  ? (r,p,s) :")
        if Player1=='r':
            print("Player1 choose \U0001FAA8")
        elif Player1=='p':
            print("You choose \U0001F4C4")
        elif Player1=='s':
            print("Player1 choose \u2702\ufe0f")
        else:
            print("Choose the correct option")
            break
        Player2=input("Player2 : Choose Rock , Paper  or Scissors  ? (r,p,s) :")
        if Player2=='r':
            print("Player2 choose \U0001FAA8")
        elif Player2=='p':
            print("Player2 choose \U0001F4C4")
        elif Player2=='s':
            print("Player2 choose \u2702\ufe0f")
        else:
             print("Player1 the correct option")
        if (Player1=='r' and Player2=='r') or (Player1=='r' and Player2=='r') or (Player1=='r' and Player2=='r'):
            print("Its a tie")
        elif(Player1=="r" and Player2=="s"):
                print("Player1 Won")
        elif(Player1=="r" and Player2=="p"):
                print("Player2 Won")
        elif(Player1=="s" and Player2=="r"):
                print("Player2 Won")
        elif(Player1=="s" and Player2=="p"):
                print("Player Won")
        elif(Player1=="p" and Player2=="r"):
                print("Player1 Won")
        elif(Player1=="p" and Player2=="s"):
                print("Player2 Won")
        val=input("Do you want to continue ?(y/n) :").lower()
        if val=='n':
            break


