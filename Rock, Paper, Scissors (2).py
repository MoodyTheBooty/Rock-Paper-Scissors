import random
name = input('Enter your name:  ')
ranNum = 0
done = False
global victories
global losses
global guess
guess = 0
victories = 0
losses = 0
def generate():
    global guess
    global ranNum
    ranNum = random.randint(1,3)
    if ranNum == 1:
        guess = "Rock"
    elif ranNum == 2:
        guess = "Paper"
    elif ranNum == 3:
        guess = "Scissors"
    
while done == False:
    global choice
    global guesss
    generate()
    guesss = ranNum
    if victories < 10 and losses < 10:
        choice = input("Rock (1)/ Paper(2) / Scissors(3): ")
        choice = int(choice)
        if choice == 1:
        #"Rock" or choice == "rock" or choice == "R" or choice == "r" or choice == 1 :
        #    choice = 1
            if guesss == 1:
                print("It's a tie!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
            elif guesss == 2:
                losses += 1
                print("Opp got a point!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
            elif guesss == 3:
                victories += 1
                print(name + "  just got a point!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
        elif choice == "Paper" or choice == "paper" or choice == "P" or choice == "p" or choice == 2 :
            choice = 2
            if guesss == 1:
                victories += 1
                print(name + "  just got a point!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
            elif guesss == 2:
                print("It's a tie!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
            elif guesss == 3:
                losses += 1
                print("Opp got a point!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
        elif choice == "Scissors" or choice == "scissors" or choice == "S" or choice == "s" or choice == 3 :
            choice = 3
            if guesss == 1:
                losses += 1
                print("Opp got a point!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
            elif guesss == 2:
                victories+= 1
                print(name + " just got a point!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
            elif guesss == 3:
                print("It's a tie!!" + " Opp: " + guess + "\n" + str(victories) + " / " + str(losses))
        else:
            print("Ok lmao try it one more time")
