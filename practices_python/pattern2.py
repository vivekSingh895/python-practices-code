# pattern traimgale---------
print("pattern triangle --------------")
for i in range(1,6):
    for j in range(5,i-1,-1):
        print("* ",end="")
    print()    

# pattern number but different ---------
print("pattern triangle --------------")
for i in range(1,6):
    for j in range(1,i+1):
        print(i , end=" ")
    print()        

# pattern triangle --------------
print("pattern triangle --------------")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()        

#pattern triangle table --------------
print("pattern triangle table --------------")    

for i in range(1,6):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()    

# New style pattern -------------------
print("New pattern --------------")    

for i in range(1,6):
    for j in range(1,i+1):
        print("* ",end="")
    print()    
for k in range(1,6):
    for l in range(4,k-1,-1):
        print("* ",end="")
    print()        