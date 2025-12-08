def myfunc(name):
    
    return ''.join([ name[i].upper() if i%2==0 else name[i].lower()  for i in range(len(name))])

# name = 'gopiram'

# mylist = ''.join([ name[i].upper() if i%2==0 else name[i].lower()  for i in range(len(name))])

# print(mylist)

name = 'gopiram'

print(myfunc(name))

