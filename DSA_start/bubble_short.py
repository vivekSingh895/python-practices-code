num = [3,2,5,4,7,6,8,9,4,2,1]

def bubble_sort(n):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i] > n[j]:
                n[i] , n[j] = n[j],n[i]

bubble_sort(num)
print(num)                