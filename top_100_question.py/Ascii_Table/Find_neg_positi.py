# <<<<<= Find Negative or POsitive Number =>>>>>>
def neg_posi(n):
    if(n >= 0):
        print("the number is positive")

    else:
        print("the number is negative ")         

# <<<<<= Find Odd or Even Number =>>>>>>

def odd_even(n):
    if(n %2 == 0):
        print("The number is Even")      
    else:
        print("the number is Odd ")      

n = int(input("enter a number : "))
#neg_posi(n) 
odd_even(n)