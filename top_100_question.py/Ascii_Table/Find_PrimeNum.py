# Find prime number 1 to 'n'

def prime_num(n):
    a=0
    for i in range(1 , n+1):
        count = 0
        for j in range(1 , n+1):
            if(i %j == 0):
                count += 1
        if(count == 2):
            print(i)   

#prime_num(100)           
#      

# Find prime number in given range =>

def prime_in_range(n1,n2):
    for i in range(n1,n2+1):
        count = 0 
        for j in range(1, n2+1):
            if i %j == 0:
                count += 1
        if count == 2 :        
            print(i) 

#prime_in_range(10,20)

# Find prime number in a given range

def isRange_prime(a,b):
    
    for i in range(a,b+1):
        flage = True
        for j in range(2,int(i/2)+1):
            if i%j == 0:
                flage = False
        if flage == True:
            print(i)
        else:
            continue       

isRange_prime(10,20)
# check number is prime or not 

def check_prime(n):
    flage = True
    if n < 2:
        flage = False
    else:
        for i in range(2,n):
            if n % i == 0 :
                flage  = False
                break
        if flage == False:
            print("not prime") 
        else:
            print("prime ")    

#check_prime(6)                       
# Find prime number with squre root

def check_sqrt_primw(n):
    flage = True
    if n < 2:
        flage = False
    else:
        for i in range(2,int(pow(n, 0.5))+1):
            if n % i == 0 :
                flage  = False
                break
        if flage == False:
            print("not prime") 
        else:
            print("prime ")  

#check_sqrt_primw(6)              


# Find prime with recursion
# 
def prime_recursion(n , item = 2):
    if n == item:
        return  True
    if n % item == 0:
        return False
    if n < 2 :
        return False
    return prime_recursion(n, item + 1)

if prime_recursion(91) == True:
     print("Prime")
else:
    print("Note Prime ")