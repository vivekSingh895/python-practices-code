#method 1.
# Find N natural number of sum using Loop
def sum_of_nNumber(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print("Sum of n Nutural Number Loop  : ",sum)    

# Method 2.
#Find N natural number of sum using recursion
print()
def sum_natural_num(n):
    if(n <= 0):
        return 0
    return n + sum_natural_num(n-1)


n = int(input("Enter any natural Number : "))
sum_of_nNumber(n)    
result = sum_natural_num(n)
print("sum of Number Recursion : ",result)