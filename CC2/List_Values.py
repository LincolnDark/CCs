mylist = [1,2,3,6,8,12,20,32,46,85]
for i in mylist
if i >5:
print(i)

i = next((i for i in mylist if i < 5), print i)


# AD Your code is in python2 form, you need to fix this for python 3