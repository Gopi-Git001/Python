mylist = [1,2,3,4,5,6,7,8,9]

print(len(mylist))

print(mylist[::])

print(mylist[::2])

print(mylist[::-1])


mylist[0] = 4674

print(mylist)

#properties


mylist.append(62748)

print(mylist)
#we can add pop item using indexing
mylist.pop()

print(mylist)


mynewlist = [11,22,33]

mylist.extend(mynewlist)

print(mylist)

