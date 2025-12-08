def myfunc(word):
    
    return ' '.join(word.split()[::-1])

print(myfunc('I am home'))