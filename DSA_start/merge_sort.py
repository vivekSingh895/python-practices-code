nums = [3,6,5,1,9,2,4,11,0,8]
left = [1,3,5,7]
right = [2,4,6,8,9]

def merge_arr(left , right):
    result = []
    i ,j =0,0
    n = len(left)
    m = len(right)
    while(n > i and m > j):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while(i < n):
            result.append(left[i])
            i += 1
    if m > j :
        while(j < m):
            result.append(right[j])
            j += 1
    return result

def merg_short(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left = num[:mid]
    right = num[mid:]
    left_indx = merg_short(left)
    right_indx = merg_short(right)
    return merge_arr(left_indx , right_indx)
print(merg_short(nums))
            

