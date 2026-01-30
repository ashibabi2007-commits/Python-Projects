id=[1634,1638,1928,1994,1887,1547,1549]
empid=[]    
empsalary=[]
empdaysworked=[]
empsaless=[]
n=int(input("Enter the Employee ID: "))
if n in id:
    print("Employee ID found:")
    print("Enter your password to proceed")
    p=input("Enter Password: ")
    if n==1634 and p=="emp@1634":
        print("Access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.") 
        salary=float(input("Enter your salary: "))
        days_worked=int(input("Enter the number of days you worked this month: "))
        total_sales=float(input("Enter your total sales for this month: "))
        bonus=0.10*total_sales
        print("Bonus calculated:", bonus)
        tax=0.15*salary
        print("Tax calculated:", tax)
        print("Enter 0 to log out")
        logout=int(input("Enter here: "))
        if logout==0:
            print("Thank you for using the Employee Portal. Have a great day!")
    elif n==1638 and p=="emp@1638":
        print("Admin access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.")  
        print("Admin privileges enabled.")
        yn=input("Do you want to add all employee details? (yes/no): ")
        if yn.lower()=="yes":
            empid.append(input("Enter Employee ID: "))
            for i in empid:
                if i==id:
                    print("Employee ID already exists.")
                else:
                    salary=float(input("Enter your salary: "))
                    empsalary.append(float(salary))
                    empdaysworked.append(int(input("Enter the number of days you worked this month: ")))
                    empsaless.append(float(input("Enter your total sales for this month: ")))        
                    print("Employee details added successfully.")   
                    bonus=0.10*empsaless[-1] 
                    print("Bonus calculated:", bonus)
                    tax=0.15*empsalary[-1]
                    print("Tax calculated:", tax)
            print("Enter 0 to log out")
            logout=int(input("Enter here: "))
            if logout==0:
                print("Thank you for using the Employee Portal. Have a great day!")
    elif n==1928 and p=="emp@1928":
        print("Access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.")  
        salary=float(input("Enter your salary: "))
        days_worked=int(input("Enter the number of days you worked this month: "))
        total_sales=float(input("Enter your total sales for this month: "))
        bonus=0.10*total_sales
        print("Bonus calculated:", bonus) 
        tax=0.15*salary
        print("Tax calculated:", tax)
        print("Enter 0 to log out")
        logout=int(input("Enter here: "))
        if logout==0:
            print("Thank you for using the Employee Portal. Have a great day!")
    elif n==1994 and p=="emp@1994":
        print("Access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.")  
        salary=float(input("Enter your salary: "))
        days_worked=int(input("Enter the number of days you worked this month: "))
        total_sales=float(input("Enter your total sales for this month: "))
        bonus=0.10*total_sales
        print("Bonus calculated:", bonus) 
        tax=0.15*salary
        print("Tax calculated:", tax)
        print("Enter 0 to log out")
        logout=int(input("Enter here: "))
        if logout==0:
            print("Thank you for using the Employee Portal. Have a great day!")
    elif n==1887 and p=="emp@1887":
        print("Access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.")  
        salary=float(input("Enter your salary: "))
        days_worked=int(input("Enter the number of days you worked this month: "))
        total_sales=float(input("Enter your total sales for this month: "))
        bonus=0.10*total_sales
        print("Bonus calculated:", bonus) 
        tax=0.15*salary
        print("Tax calculated:", tax)
        print("Enter 0 to log out")
        logout=int(input("Enter here: "))
        if logout==0:
            print("Thank you for using the Employee Portal. Have a great day!")
    elif n==1547 and p=="emp@1547":
        print("Access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.")  
        salary=float(input("Enter your salary: "))
        days_worked=int(input("Enter the number of days you worked this month: "))
        total_sales=float(input("Enter your total sales for this month: "))
        bonus=0.10*total_sales
        print("Bonus calculated:", bonus) 
        tax=0.15*salary
        print("Tax calculated:", tax)
        print("Enter 0 to log out")
        logout=int(input("Enter here: "))
        if logout==0:
            print("Thank you for using the Employee Portal. Have a great day!")
    elif n==1549 and p=="emp@1549":
        print("Access Granted")
        print("Welcome to the Employee Portal")
        print("Here you can access your work resources and information.")
        print("Remember to log out when you're done to keep your account secure.")  
        print(empid)
        print(empsalary)
        print(empdaysworked)
        print(empsaless)
        print("Enter 0 to log out")
        logout=int(input("Enter here: "))
        if logout==0:
            print("Thank you for using the Employee Portal. Have a great day!")   
    else:
        print("Access Denied: Incorrect Password")
else:
    print("Employee ID not found")
