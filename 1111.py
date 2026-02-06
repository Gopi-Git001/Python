# s = 'Hello world '
# t = s.upper()
# print(t)
# print(t.split())
# number = 1.2345

# print('his number is : {n:1.2f}'.format(n=number))


# my_list = [1,2,3,4,5,8,10,9,7]

# my_list.sort()
# print(my_list)

# my_new_list = my_list.sort()
# print(my_new_list)
# print(type(my_new_list))


# #we don't assign a sorted list to new variable

# my_list.append(11)
# print(my_list)
# popped_item = my_list.pop()
# print(my_list)
# print(popped_item)

# list1 = [1,2,3]
# list2 = [1,2,3]
# list3 = [1,2,3]

# mylist = [list1,list2,list3]
# print(mylist[1])
# print(max(my_list))
# print(min(my_list))


my_dict = {'key1':1,'key2':2,'key3':3}

print(my_dict['key1'])

print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())

for key in my_dict.items():
    print(key)


list = [key for key in my_dict.items()]
print(list)

print([i for i in my_dict.values()])

my_dict['key4'] = 4

print(my_dict)

#Nested 

my_new_dict = {'key1':{'key2':{'key3':3},'key2':2,'key3':3}}
