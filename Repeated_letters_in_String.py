mystring = 'mississipirmanagarramkumar'
mylist = tuple(list(mystring))
print(mylist)


newlist  = set([i  for i in mylist if mylist.count(i) >1])
print(newlist)



