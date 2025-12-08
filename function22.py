def myfunc(mylist):
    
    x = 0
    
    add = True
    
    for i in mylist:
        while add:
            
            if i!=6 :
                
                x+=i
                break
                
            else:
                
                add = False
                
        while not add:
            
            if i!=9:
                
                break
            
            else:
                add = True
                break
    return x

                
                
mylist = [0,0,6,1,2,9,0]

print(myfunc(mylist))


        