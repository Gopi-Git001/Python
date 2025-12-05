name = 'gopiram'

n = ''

for i in range(len(name)):
    
    if i%2 == 0:
        
        n+=name[i].upper()
        
    else:
        n+=name[i].lower()
        
print(n)


t = ''.join([x.upper() if i%2 == 0 else x.lower() for i,x in enumerate(name)])
print(t)

#Nested list comprehension


t = [x*y for x in [1,2,3] for y in [1,2,3]]
print(t)


mylist = [x for x in 'Hello world']

print(mylist)

