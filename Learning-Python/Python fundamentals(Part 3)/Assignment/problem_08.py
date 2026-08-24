# Q8. Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]

#1.
list1 = [1, 2, 3, 4]
list1 = set([1, 2, 3, 4])
list2 = [5, 6, 7, 8]
list2 = set([5, 6, 7, 8])
if(list1.intersection(list2)==set()):
    print("share no common elements")
else:
    print("share common elements")

#2.
list1 = [1, 2, 3]
list1 = set([1, 2, 3])
list2 = [3, 4]
list2 = set([3, 4])
if(list1.intersection(list2)==set()):
    print("share no common elements")
else:
    print("share common elements")
