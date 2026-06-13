num = [2,5,3,1]
x = len(num)+1
def find_missing(n):
    sum ,sum1 = 0,0
    for i in range(len(n)):
        sum = (x*(x+1))//2
        sum1 += n[i]
    miss = sum - sum1
    return miss    

print(find_missing(num))    