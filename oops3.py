class Circle():
    
    pi = 3.14
    
    def __init__(self,radius):
        self.radius = radius
        self.area = radius*radius*self.pi
        
    def get_circumference(self):
        
        return self.radius*self.pi*2
    
my_circle = Circle(10)

print(my_circle.get_circumference())

        