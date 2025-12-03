# Use range() to print all the even numbers from 0 to 10.
#method 1
mylist = [i for i in range(11) if i%2 == 0]
print(mylist)

#method2

newlist = []
for i in range(11):

    if i%2 == 0:
        newlist.append(i)
    else:
        pass
print(newlist)
