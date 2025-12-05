# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
print(10**2/4 + (150 -125)*2 + 25.25)


#What would you use to find a number’s square root, as well as its square?
from math import sqrt 

print(100**0.50)
print(sqrt(100))


#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

string = 'hello'

print(string[1])

#Reverse the string 'hello' using slicing:

print(string[::-1])

#Build this list [0,0,0] two separate ways.

print([0]*3)

print([0,0,0])

#Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

#Sort the list below:

list4 = [5,3,4,6,1]

list4.sort() # sort is a placing function It doesn't support to  assigning to a new variable 

print(list4)  


#Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}

print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'])


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2])

#Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))

