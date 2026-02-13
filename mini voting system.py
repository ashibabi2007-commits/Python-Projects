n=int(input("Enter your age:"))
count1=0
count2=0
count3=0
if n>=18:
    print("you are eligible to vote ")
    print("Chosose your candidate:")
    print("1.Ashish Dash-(sign-Bus)")
    print("2.Pranjal Paramita Sahu-(sign-Fight)")
    print("3.Bibekandan Tripathy-(sign-Sleep)")
    c=int(input("Enter the candidate number:"))
    if c==1:
        print("you have successfully voted")
        count1+=1
    elif c==2:
        print("you have successfully voted")
        count2+=1
    elif c==3:
        print("you have successfully voted")
        count3+=1
    else:
        print("Invalid candidate number")
    print(f"Total votes for Ashish Dash: {count1}")
    print(f"Total votes for Pranjal Paramita Sahu: {count2}")
    print(f"Total votes for Bibekandan Tripathy: {count3}")
    if count1>count2 and count1>count3:
        print("Ashish Dash wins the election!")
    elif count2>count1 and count2>count3:
        print("Pranjal Paramita Sahu wins the election!")
    elif count3>count1 and count3>count2:
        print("Bibekandan Tripathy wins the election!")
    else:
        print("It's a tie!")
else:
    print("you are not eligible to vote")