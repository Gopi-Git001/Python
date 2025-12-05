def myfunc(mylist):
    
    even_numbers = []
    
    for i in mylist:
        
        if i%2==0 :
            
            even_numbers.append(i)
            
        else:
            pass
        
    return even_numbers


mylist = [1,2,3,4]

print(myfunc(mylist))

    
    