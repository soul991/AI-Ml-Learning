s = {1, 2, 3, 3, 4}

#Add method
s.add(5)
print(s)

#Remove method
s.remove(4)
print(s)

#remove random value 
s.pop()
print(s)

#Empty set 
s.clear()
print(s)

#uninon method
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}
print(s1.union(s2))
print(s1.intersection(s2))