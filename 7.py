name = 'gggggggggg'

#print(set(name.split()))

#print(name.split())

for i in name:
    #print(i)
    pass
##print(set(list(name)))



t = tuple(name)

#print(t)

l = []

for i in t:
    if t.count(i) >1:
        
        l.append(i)
    else:
        pass
print(l)

print(set(l))

    