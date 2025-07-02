mystring = 'mississipirmanagarramkumar'
mylist = tuple(list(mystring))
print(mylist)
newlist  = set([i  for i in mylist if mylist.count(i) >1])
newlist2  = set([(i,mylist.count(i))  for i in mylist if mylist.count(i) >1])
print(newlist)
print(newlist2)


existlist = [(i,mylist.count(i)) for i in mylist] 

# print(existlist)


# for i in mylist:
#     print(i,mylist.count(i))
