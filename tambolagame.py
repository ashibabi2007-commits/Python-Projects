import random
def gticket():
    return random.sample(range(0,91),9)
while True:
    print("\n--------------------- TAMBOLA GAME ------------------------------")
    print("1. Start Game")
    print("2. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        while True:
            players =int(input("\nEnter number of players: "))
            luck =gticket()
            print("\nApka luck:")
            print(luck)
            print("\nkhiladiyon ka Tickets:")
            for i in range(1,players+1):
                khiladi =gticket()
                print(f"khiladi {i} Ticket: {khiladi}")
            print("kon jeeta bhai batao?")
            winner =int(input("Enter the winning player number: "))
            print(f"\nCongratulations! khiladi {winner} tu jeet gaya re.......!")
            print("\nAur ekk Baar khelega kya?")
            print("1. Yes")
            print("2. No")
            again =int(input("Enter your choice: "))
            if again==1:
                print("Majja aaraha hai! Chalo phir se khelte hain.")
                continue
            else:
                print("Returning to main menu...")
                break
    elif choice == 2:
        print("Exiting game...")
        break
    else:
        print("Invalid choice! Try again.")
