name = 'gopiram'

NewName = ''

for i in range(len(name)):
    #print(i)
    
    if i%2 == 0:
        NewName=NewName+name[i].upper()
    else:
        NewName=NewName+name[i].lower()
    
print(NewName)


name = 'Hello world' 

print(name[-3])

another_list = ['Gopi']
new = name.split()

print(name.split())
print(' '.join(new))



