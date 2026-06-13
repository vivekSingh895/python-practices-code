# Method 1.

num = [1,1,2,3,4,5,3,2,5,6,7,6,1,2]

def frquency_count(num):
    dict = {}
    for i in range(len(num)):
        if num[i] in dict:
            dict[num[i]] += 1 

        else:
            dict[num[i]] = 1 
    return dict

print(frquency_count(num))

# Method 2.

def frquenc(num):
    dict = {}
    for i in range(len(num)):
        dict[num[i]] = dict.get(num[i],0)+1 
    print(dict)

frquenc(num)