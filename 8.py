with open('mytest.txt' , mode= 'w') as f:
    f.write('Hello World ')
    
with open('mytest.txt' , mode = 'r') as f:
    print(f.read())
    
with open('mytest.txt',mode='a') as f:
    f.write('It is beautiful Outside')
    
with open('mytest.txt',mode ='r') as f:
    print(f.read())
    
    
    
with open('myfile.txt' , mode = 'w+') as f:
    
    f.write('Hello World')
    
    f.seek(0)
    
    print(f.read())
    
    
    
with open('my_new_file.txt', mode = 'w+') as g:
    
    g.write('Hello Gopi How are you!')
    
    g.seek(0)
    
    print(g.read())