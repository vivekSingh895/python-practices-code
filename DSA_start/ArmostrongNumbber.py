n   = 153
def armstrongNum(n):
    count = len(str(n))
    num = n 
    total = 0
    while(num > 0 ):
        rem = num % 10 
        result = pow(rem , count) # count = 3
        total += result # 27 + 125 + 1
        num = int(num / 10)
    return total 
    
if armstrongNum(n) == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number ")       
     