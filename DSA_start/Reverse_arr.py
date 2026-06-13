num = [3,4,7,3]
a = num
a.reverse()
print(a)
def reverseNum(num,left , right):
    while left <= right:
        temp = num[left]
        num[left] = num[right]
        num[right] = temp
        left += 1
        right -= 1

#reverseNum(num , 1 ,2)
#print(num)

# Using Recursion 

def reverse_recursion(num , left , right):
    if left >= right:
        #print(num)
        return
    num[left] , num[right] = num[right],num[left]
    reverse_recursion(num , left+1 , right-1)
    return num

x = reverse_recursion(num , 1 , 2)
