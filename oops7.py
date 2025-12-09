def ask_a_number():
    
    while True:
        
        try:
            
            result = int(input('Please provide your results:'))
            
        except:
            
            print("you provided wrong details ")
            continue
        else:
            break
        
    return result

print(ask_a_number())

        