class Animal():
    
    def __init__(self,name,breed,number):
        self.name = name
        self.breed = breed 
        self.number = number 
        
        
    def speak(self):
        return f"Hello my name is {self.name}"
    
    
class Dog(Animal):
    
    def speak(self):
        
        return f" Hello My breed is {self.breed}"
    
class Cat(Animal):
        
        def speak(self,number):
            
            return f" Hello I'm {self.name} and My number is {number}"
    
    
my_dog = Dog('Jhonny','Huskie',4674)

print(my_dog.speak())

my_cat = Cat('jose','portila',4674)

print(my_cat.speak(88))

