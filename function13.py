# def myfunc(a,b):
#     if a%2==0 and b%2==0:
#         return min(a,b)
    
#     else:
         
#          return max(a,b)
     
# print(myfunc(1,2))

def myfunc(a,b):    
    return min(a,b) if a%2==0 and b%2==0 else max(a,b)
print(myfunc(1,2))
