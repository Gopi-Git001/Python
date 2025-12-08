def myfunc(*args):
    
    return [x for x in args if x%2==0]


print(myfunc(1,2,3,4,5,6))