num = [4,6,3,8,1,9,5,2]

def selection_sort(n):
    for i in range(len(n)):
        min_indx = i
        for j in range(i+1,len(n)):
            if n[min_indx] > n[j]:
                min_indx = j
        n[i],n[min_indx] = n[min_indx],n[i]        

selection_sort(num)
print(num)        