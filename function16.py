def myfunc(name):
    
    # return ''.join([x for x in name])
    return name[:3].capitalize()+name[3:].capitalize()

print(myfunc('gopiram'))

print(myfunc('macdonald'))