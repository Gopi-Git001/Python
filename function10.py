# def myfunc(*args):
    
#     return sum(args)


# print(myfunc(1,2,3,4,5))


def myfunc(*args):
    
    for i in args:
        
        if i%2 ==0:
            
            return True
    else:
        
        return False 
    


print(myfunc(1,5,3))