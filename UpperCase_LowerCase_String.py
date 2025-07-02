mystring = 'gopiram'

# g  = ''

# for i in range(len(mystring)):

#     if i%2 == 0:
#         g = g+mystring[i].upper()
#     else:
#         g = g+mystring[i].lower()

# print(g)


# mylist = [g+mystring[i].upper() if i%2== 0 else g+mystring[i].lower() for i in range(len(mystring))]
# print(mylist)

mylist = ''.join([mystring[i].upper() if i%2 == 0 else mystring[i].lower() for i in range(len(mystring))])
print(mylist)