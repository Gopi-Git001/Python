# def myfunc(a,b,c):
    
#     if sum(a,b,c)<=21:
        
#         return sum(a,b,c)
#     else:
#         return False
    
# print(myfunc(1,1,1))




def myfunc(*nums):
    
    if sum(nums) <= 21 :
        return sum(nums)
    
    elif sum(nums)>21 and 11 in nums:
        
        return sum(nums)-10
    else:
        
        return 'BUST'
    
    
print(myfunc(11,11,13))