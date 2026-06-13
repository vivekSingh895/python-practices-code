num = [5,2,7,2,9,4,2,7]

def insertion_sort(n):
    for i in range(1,len(n)):
        key = n[i]
        j = i-1
        while(j >= 0 and key <  n[j]):
            n[j+1] = n[j]
            j -=1
        n[j+1] = key

insertion_sort(num)
print(num)        