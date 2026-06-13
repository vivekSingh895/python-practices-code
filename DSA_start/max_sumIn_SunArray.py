num = [1,-3,-5,6,-3,-2,-1]

def find_max_subarray(arr):
    n = len(arr)
    maxi = -999999
    total = 0
    for i in range(0,n):
        total += arr[i]
        maxi = max(maxi , total)
        if total < 0:
            total = 0
    return maxi
print(find_max_subarray(num))        