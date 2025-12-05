#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

print(list([x for x in st.split() if x[0]=='s']))

#Use range() to print all the even numbers from 0 to 10.

print(list(x for x in range(0,10) if x%2==0))

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print(list(x for x in range(1,50) if x%3==0))

#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

print(list('even!' if  len(x)%2==0 else x for x in st.split()  ))


#Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".



for i in range(1,100):
    
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3 ==0:
        print('Fizz')
    elif i%5 ==0 :
        
        print('Buzz')
        
    else:
        pass
    
     


print(['FizzBuzz' if i%3==0 and i%5==0 else 'Buzz' if i%3 == 0 else 'Fizz' if i%5==0 else i  for i in range(1,100) ])


#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

print([x[0] for i,x in enumerate(st.split())])
