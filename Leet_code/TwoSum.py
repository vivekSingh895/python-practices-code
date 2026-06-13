
num = [2,7,5,8,3]
target = 9

def twoSum(num , target):
    has = {}
    for i,num in enumerate(num):
        if target - num in has:
            return [has[target - num],i]
        has[num] = i
    return [] 

print(twoSum(num,target))   
       

def twoSum1(num1 , target1):
    has_map = {} # { 2 : 0 , 7 : 1 , 5 : 2 , 8 : 3, 3 : 4}
    for i in range(len(num1)):
        if target1 - num1[i] in has_map:
            return [has_map[target1 - num1[i]],i] # return[ 2 , 4]
        has_map[num1[i]] = i
    return []        

print(twoSum1(num,target))   
       