def myfunc(num):
    return num**2

print(myfunc(2))


num =2

print((lambda num: num**2)(num))


square = lambda num: num**2

print(square(num))




sum = lambda a,b : a+b

print(sum(1,2))


mylist = [1,2,3,4,5,6]
print(list(map((lambda num:num**2),mylist)))



