# Q3. Input two lists of integers from the user. Merge them into one list and sort theresult.
# Eg:-
# list1 = [1, 2, 7] list2 = [2, 4, 5]
# result = [1, 2, 3, 4, 5, 7]
print("input the integars for list1")
i1 =int(input("Input i1: "))
i2 =int(input("Input i2: "))
i3 =int(input("Input i3: "))
print("input the integars for list2")
i4 =int(input("Input i4: "))
i5 =int(input("Input i5: "))
i6 =int(input("Input i6: "))
list1= [i1, i2, i3]
list2=[ i4, i5, i6]
result = list1+list2
result.sort()
print(result)