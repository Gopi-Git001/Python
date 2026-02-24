#List Comprehension
mylist = [1,2,3,4,5,6,7,8,9]
print([i for i in mylist if i%2 ==0])

#Function calling
def myfunc(name):   
    return ''.join([char.upper() if i%2 ==0  else char.lower() for i ,char in enumerate(name)])
print(myfunc('gopiram'))


def  myfunc_1(mylist):
    new_list = []
    for i in mylist :
        if i %2 ==0:
            new_list.append(i)
        else:
            print("odd")
    return new_list

print(myfunc_1(mylist))


