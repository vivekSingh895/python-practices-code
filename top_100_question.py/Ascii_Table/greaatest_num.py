a = int(input("enter first number : "))
b = int(input("enter first number : "))
c = int(input("enter first number : "))
#<<<<<<<<=  find Greatest of Two Number <<<<<<<<=

#find greatest number 
# Method 1.

def greatest_twoNum(num1 , num2):
    print("if else statment ")
    if(num1 > num2):
        print("greatest number ",num1)
    elif(num1 < num2):
        print("greatest  number ",num2)
    else:
        print("invalid number ")    

           
# greatest two number usung ternary oprator
# Method 2.

def  greatest_with_ternary(a,b):
    print("ternary oprator ")
    x = print("greatest value ",a) if(a > b) else print("greatest  value ",b)

   

# using inbilt function max 
# Method 3.

def find_max(n1,n2):
    print("inbilt function")
    a = max(n1,n2)
    print("greatest value ",a)

# find if else statment
greatest_twoNum(a,b) 
#ternary statment
greatest_with_ternary(a,b)
# use  biltin function 
find_max(a,b) 


#<<<<<<<<=  find Greatest of Three Number <<<<<<<<=
print("<<<<<<<<=  find Greatest of Three Number <<<<<<<<=\n")

#find greatest number 
# Method 1.
def find_greatest(a,b,c):
    print("if else statment ")
    if(a > b and a > c):
         print("greast number ",a)
    elif(b > a and b > c):
        print("greast number ",b)
    else:
         print("greast number ",c)


#find greatest number using nested condition
# Method 2.
def nested_max_find(n1,n2,n3):
    print("nested method find max ")
    if(n1 > n2):
        if(n1 > n3):
             print("greast number ",n1)
        else:
            print("greast number ",n3)     
    elif(n1 < n2):
         if(n2 > n3):
             print("greast number ",n2) 
         else:
             print("greast number ",n3)
                      


#using ternary method 
# Method 3.

def ternary_find_max(a ,b ,c):
    print("ternary method ")
    greter =  a if(a > b) else b
    greter =  greter if(greter > c) else  c
    print("greatest number ",greter) 


# if else statment
find_greatest(a,b,c)
# nested statment
nested_max_find(a,b,c)
#ternary oprator
ternary_find_max(a,b,c)                   