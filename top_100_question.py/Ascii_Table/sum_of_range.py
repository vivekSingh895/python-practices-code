# sum of natural number using loop
#In given range
def sum_range(x1,x2):
    sum = 0
    for i in range(x1, x2+1):
        sum += i
    print(sum)

# sum of natural number given in range 
#using recursion
def recursion_sum(n1,n2):
    if(n2 == n1):
        return n2
    return n2 + recursion_sum(n1,n2-1)


# sum using loop
sum_range(3,5)

#recursion calling
result = recursion_sum(3,5)
print(result)

    