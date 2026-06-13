num = [4,69,34,-87,-25,-23,68]

def find_max(num):
    large = num[0]

    for i in range(len(num)):
        large = max(large , num[i])
    return large

#print(find_max(num))    

def findSecond_max(num):
    large= float("-inf")
    s_large = float("-inf")
    for i in range(len(num)):
        large = max(large , num[i])
    for j in range(0,len(num)):
        if (num[j] > s_large) and (num[j] != large):
            s_large = num[j]    
    return s_large
print(findSecond_max(num))

# optimal solution 

def new_solution(num):
    large = float("-inf")
    s_large = float("-inf")

    for i in range(len(num)):
        if num[i] > large:
            s_large =  large
            large = num[i]
        elif num[i] > s_large and num[i] < large:
            s_large = num[i]    
    return s_large        


print(new_solution(num))