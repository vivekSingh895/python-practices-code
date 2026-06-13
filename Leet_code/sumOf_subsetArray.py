import numpy as np

num = np.array([-2,1,-3,4,-1,2,1,-5,4])

# long Method time Complexy O(n^2) , space complexy O(...)
def sumOfArray(num):
    sum = -99999999
    for i in range(len(num)):
        new = 0
        a =0
        for j in range(a+i,len(num)):
            new = new + num[j]
            if sum < new:
                sum = new  
            a += 1    
    print(sum) 
sumOfArray(num)




# New Method Time Complexy O(n) , space complex O(1)
# num = np.array([2,3,-4,-6,3,2,1])

def sumArray(num):
    sum = -999999
    total = 0
    for i in range(len(num)):
        total = total + num[i]
        if sum < total:
            sum = total 
        if total < 0:
            total = 0
        
    print("su ",sum)         

sumArray(num)              
