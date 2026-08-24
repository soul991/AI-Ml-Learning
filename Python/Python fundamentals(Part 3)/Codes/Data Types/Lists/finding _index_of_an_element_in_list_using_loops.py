marks = [88, 73, 93, 100, 39]
idx=0
x=93
for val in marks:
    if(val==x):
        print(f"index of {x} found at {idx}".format(idx))
        break
    idx+=1

# This method is called Linear Search