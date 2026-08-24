#method 1
# i = 1

# while (i <= 10):
#     if(i % 2 != 0):
#      print(i)
#     i += 1

# print("out of the loop...", i)


#method 2 using "Continue"

i = 1

while (i <= 10):
    if(i%2==0):
         i += 1
         continue
    print (i)
    i +=1