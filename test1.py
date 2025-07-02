# Use for, .split(), and if to create a Statement that will print out words that start with 's':

#Method 1
st = 'Print only the words that start with s in this sentence'
newstring = st.split()
#print(newstring)

for i in newstring:

    if i[0] == 's':
        print(i)

    else:
        pass
 
#Method2

mylist = [i for i in st.split() if i[0]=='s']
print(mylist)