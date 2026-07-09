list = ['hello','banana','apple','orange','papaya']
#print(len(list))
#print(list[2])
check = "empty" if len(list) == 0 else "not eempty"
#print(check)

a=[]
a = [i for i in list]

list1 = ["good", "bad", "better", "perfact", "nyc"]
# important function in list <----------

list1.append("bay")
print("append one item to end: ",list1)
print(list1.index("good"))
list1.reverse()
print("reverse of list : ",list1)
print(list1[1: 4])

list1.clear()
print("clear all item : ",list1)