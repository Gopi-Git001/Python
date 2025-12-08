def myfunc(mylist):
    
    for i in mylist:
        
        if i%2==0:
            return True
    
    return False

mylist = [1,2,3,4,5,6]

print(myfunc(mylist))



#print(list(filter(myfunc,mylist)))


def myfunc(num):
    
    if num%2 == 0:
        return True
    else:
        
        return False
    
print(list(filter(myfunc,mylist)))
