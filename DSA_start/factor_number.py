import math as s
n  = int(input("enter a Number : "))

def factor_num(n):
    num = n # time Complexty O(n))
    list = []  # space Complexty O(k)
    for i in range(1 ,num+1):
        if num % i == 0:
            list.append(i)
    return list

print(factor_num(n))        

# 2. method 
def factor(n):
    num  = n # time Comolexy O(n/2)) -> O(n)
    list = [] # space Complexty O(k)
    for i in range(1 ,(num//2)+1):
        if num % i == 0:
            list.append(i)
    list.append(num)
    return list

print(factor(n))   


# 3. method
def factor1(n):
    num = n  # time Comolexy O(n^1/2) + O(nlog(n)) , [O(10^1/2) + O(10^1/2log 10^1/2)]
    list = []  # space Complexty O(k)
    for i in range(1 , int(s.sqrt(num))+1):
        if num % i == 0 :
            list.append(i)
            x = num // i
            if x != i:
                list.append(x)
    list.sort()            
    return list
print(factor1(n))            
    