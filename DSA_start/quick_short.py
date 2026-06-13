num = [4,5,6,3,2,7,4,8,9]
def partition(num , low, high):
    pivrt = num[low]
    i , j = low , high
    while i < j:
        while pivrt >= num[i] and i <= high -1:
            i += 1
        while pivrt <= num[j] and j >= low +1:
            j -= 1
        if i < j:
            num[i] , num[j] = num[j] , num[i]
    num[low] , num[j] = num[j] , num[low]
    print("hellp",j)
    return j
def quick_short(num, low, high):
    if low < high:
        p = partition(num , low , high)
        quick_short(num , low , p-1)
        quick_short(num,p+1,high)        

quick_short(num , 0,len(num)-1)                
print(num)