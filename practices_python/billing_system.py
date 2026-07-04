# using while loop for billing system 

while True:
    name = str(input("enter yur name: "))
    age = int(input("enter age : "))
    mobile_no = int(input("enter your mobile no : "))
    total =0
    while True:
        print("-"*50)
        print("Enter prise and quantity")
        prise = float(input("enter prise of item: "))
        quantity = int(input("enter quantity of intem : "))
        total += quantity* prise
        print("-"*50)
        repeat = input("do you want buy more item (yes / no)")

        if repeat == "no" or repeat =="No":
            break
        else:
            continue

    print("-"*40)        
    print("Customer name: ",name)
    print("Customer age: ",age)
    print("Customer mobile No: ",mobile_no)
    print("total prise: ",total) 
    print("-"*40)
    repeat1 = input("do you wan to add more customer yes/no ")

    if repeat1 == "no" or repeat1 == "N0":
        break
    else:
        continue