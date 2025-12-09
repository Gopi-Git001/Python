class Animal():
    
    def __init__(self,name,breed):
        
        self.name = name 
        self.breed = breed
        
    def speak(self):
        
        return f"My name is {self.name}"
        
class Dog(Animal):
    
    def __init__(self,name,breed,spots):
        Animal.__init__(self,name,breed)
        
        self.spots= spots
        
    def speak(self):
        
        return f" I have {self.spots}"
    
class Cat(Animal):
    
    def __init__(self,name,breed,number):
        Animal.__init__(self,name,breed)
        self.number = number
        
    def speak(self):
        
        return f"My number is {self.number}"

my_animal = Animal('sammy','Huskie')
my_dog = Dog('jhonny','Eve','Black and White')
my_cat = Cat('robbin','tommy',4674)

print(my_dog.breed) 

print(my_dog.name)

print(my_dog.speak())

print(my_animal.speak())

print(my_cat.name)

print(my_cat.breed)

print(my_cat.number)

print(my_cat.speak())


mylist = [my_animal,my_cat,my_dog]

for i in mylist:
    
    print(i.speak())
    
    

      
        