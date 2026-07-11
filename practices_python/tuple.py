tup = "good",
#print(type(tup))
a = ("banana", "mango", "apple")
#print(type(a))

new_tuple = tuple(("batman","spiderman", "ironman"))
#print(type(new_tuple))

print("Slicing : ", new_tuple[1:4])

list = list(new_tuple)
list.append("Captain America")
tuple(list)
print(type(list))

print("hell changes file")