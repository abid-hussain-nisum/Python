set = {1,2,3,4,5,9,0,3,1,2,3}
set1 = {22,34,56,77,75}
print(set)
set.add(33)
set.remove(1)
a = set.pop()
print(a)
print(set)
set.update(set1)
print(set)
set.clear()
print(set)

a = {1,2,3}
b = {2,3,4}
print(a.difference(b)) # a-b
print(b.difference(a)) # b-a
print(a.union(b)) # aub
print(a.intersection(b)) # anb
