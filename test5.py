# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

#method1
mylist = [i[0] for i in st.split() ]
print(mylist)

#method2
new = []
for i in st.split():
    new.append(i[0])

print(new)

