# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#method1
mylist = [i for i in range(1,50) if i%3 ==0 ]
print(mylist)

#method 2

newlist = []

for i in range(1,50):
    if i%3 == 0:
        newlist.append(i)
    else:
        pass
print(newlist)

