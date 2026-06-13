# Head recursion 1 to n and n to 1 

def num_print(i,n):
    if i > n:
        return
    print(i)
    num_print(i+1,n)

#num_print(1,5) 
print()   

# using single varival

def num_count(n):
    if n == 6:
        return
    print(n)
    num_count(n+1)

#num_count(1)  


# =>>>>>> tail Recursion <<<<<<<<=
# # 1 to n and n to 1 

def tail_numCount(i ,n):
    if i > n:
        return
    tail_numCount(i+1 ,n)
    print(i)

#tail_numCount(1,5)    
print()

# Method 2. 

def numCount(i ,n):
    if n == i:
        return
    numCount(i ,n-1)
    print(n)

#numCount(0,5)

# Method second one parameter

def tail_Count(n):
    if n == 0:
        return 0
    print("hello",tail_Count(n-1))
    print(n)

#tail_Count(5)          

def head_Count(n):
    if n == 0:
        return 0
    print(n)
    head_Count(n-1)
head_Count(5)   