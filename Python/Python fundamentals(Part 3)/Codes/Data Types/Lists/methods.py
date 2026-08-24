marks = [88, 73, 93, 100, 39]

marks.append(98) #By default, add the new value at the end of the list
print(marks)

marks.insert(5,95 ) #First. the index and then the value
print(marks)

marks.sort() #By deefault sort the elements in the increasing order
print(marks)
#To reverse the the order of the elements on the list
marks.sort(reverse=True) 
print(marks)

#To reverse the list without any order
marks = [88, 73, 93, 100, 39]
marks.reverse()
print(marks)