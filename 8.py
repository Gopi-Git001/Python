with open('mytest.txt' , mode= 'w') as f:
    f.write('Hello World ')
    
with open('mytest.txt' , mode = 'r') as f:
    print(f.read())
    
with open('mytest.txt',mode='a') as f:
    f.write('It is beautiful Outside')
    
with open('mytest.txt',mode ='r') as f:
    print(f.read())
    
    
    
    