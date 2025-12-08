# def myfunc(mylist):
    
    
#     return set([True if (mylist[i]==3 and mylist[i+1]==3) else False for i in range(len(mylist))])

    
# print(myfunc([1,3,3,4,5]))




def myfunc(nums):
    
    for i in range(len(nums)):
        
        if nums[i] ==3 and nums[i+1]==3:
            return True
        
    else:
        return False


nums = [1,2,3,4,3,4,3,6]

print(myfunc(nums))

