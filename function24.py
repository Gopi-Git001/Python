def user_choice():
    
    choice = 'wrong'
    
    acceptable_range = range(0,10)
    
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
        choice = input('Please choose a position (0,10):')
        
        if choice.isdigit() == False:
            print('please choose an Integer')
            
        if choice.isdigit()==True:
            
            if int(choice) in acceptable_range:
                
                within_range = True
                
            else:
                
                within_range = False
                
    return int(choice)


print(user_choice())

