print("welcome to rock paper scissor game")
import random
while True:
    score=0
    n=random.randint(1,3)
    if n==1:
        ch="rock"
    elif n==2:
        ch="paper"
    else:
        ch="scissor"
    n1=int(input("What you choose? 1.rock 2.paper 3.scissor:"))
    if n1==1:
        print("you: rock")
        if ch=="rock":
            print("computer: rock")
            print("tie")
        elif(ch=="paper"):
            print("computer: paper")
            print("you lose")
            score-=1
    elif n1==2:
        print("you: paper")
        if ch=="paper":
            print("computer: paper")
            print("tie")
        elif(ch=="rock"):
            print("computer: rock")
            print("you win")
            score+=1
        elif(ch=="scissor"):
            print("computer: scissor")
            print("you lose")
            score-=1
    else:
        print("you: scissor")
        if ch=="scissor":
            print("computer: scissor")
            print("tie")
        elif ch=="rock":
            print("computer: rock")
            print("you win")
            score+=1
        elif(ch=="paper"):
            print("computer: paper")
            print("you lose")
            score-=1
    print("your score is:",score)
    print("thank you for playing the game")
    print("do you want to play again? (yes/no)")
    play_again=input()
    if play_again.lower()!="yes":
        break

