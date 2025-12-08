class Dog():
    
    def __init__(self,breed,name,spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots
        
    def bark(self,number):
        
        print(f'woof! my name is {self.name} and my number is {number}')
        
        
my_dog = Dog('Huskie','Sammy','No spots')

print(my_dog.bark(4674))

