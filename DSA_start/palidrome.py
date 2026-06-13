str = "nitin"
# 1. Method
def check_palidrom(str):
    a = ""
    for i in range(len(str)-1,-1,-1):
        a += str[i]
    if str == a:
        print("True") 
    else:
        print("False")       

#check_palidrom(str)        

# 2 Method 

def recur_palidrome(str , l,r):
    if l <= r:
        return True
    if str[l] != str[r]:
        return False 
    
    return recur_palidrome(str , l+1,r-1)
    
d = recur_palidrome(str , 0,len(str)-1)
print(d)    