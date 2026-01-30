r=10000000000
id=[9132,1928,1994,1887]
n=int(input("Enter the atm pin number: "))
while True:
    if n not in id:
        print("XXXX Invalid Pin Number XXXX \n Please enter the valid pin number")
        n=int(input("Enter the atm pin number: "))
        if n not in id:
            continue
    else:
        print("                                         WELCOME TO THE APNAKHATA BANK")
        c=int(input("Enter what transaction you want to do: \n 1.Deposit \n 2.Withdrawl \n 3.Balance \n4.Transaction History  \n5.Exit***********************************************************\n"))
        while True:
                if c==1:
                    a=int(input("Enter what amount to be deposit in the account: "))
                    def deposit(d,s):
                        e=s+d
                        print("The amount has been deposited in your account.")
                        print("The current account balance is: ",e)   
                        print("***********************************************************")
                    deposit(a,r)
                elif c==2:
                    b=int(input("Enter what amount to be withdrawl from the account: "))
                    def withdraw(w,m):
                        if w<r:
                            f=m-w
                            print("The amount has been withdrawl from your account.")
                            print("The current account balance is: ",f)
                            print("***********************************************************")
                        else:
                            print("XXXX The account has low balnce XXXX \n Hence the transaction has been declined")
                            print("***********************************************************")
                    withdraw(b,r)
                elif c==3:
                    print("Your current balance is: ",r)
                    print("***********************************************************")
                elif c==4:
                    print("Transaction History: ",)
                elif c==5:
                    print("Transaction has been completed")
                
                d=input("do you want to start transaction again? (y/n): ")
                if d=='y' or d=='Y':
                    c=int(input("Enter what transaction you want to do: \n 1.Deposit \n 2.Withdrawl \n 3.Balance \n***********************************************************\n"))
                else:
                    print("********** THANK YOU FOR USING THE ATM SERVICE **********")
                    break 
        else:
            break
        break
