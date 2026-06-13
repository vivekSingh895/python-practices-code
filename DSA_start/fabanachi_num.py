

def fabnachi(n):
    if n == 0 or n == 1:
        return n
    return fabnachi(n-1) + fabnachi(n-2) 
a = fabnachi(6) # 0 1,1,2,3,5,8,13
print(a)