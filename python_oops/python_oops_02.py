#in this module we will study abioout the polymorphism and oops concepts in details:
from abc import ABC
from abc import abstractmethod

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary



    def get_info(self):
        return f"Employee name is {self.name}, and its salary is {self.salary}"
    

class Managers:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Manager name is {self.name} and its salary is {self.salary}"
    

    
employees = [
    Employee("Apoorv", 1000000),
    Employee("Rohan", 500000),
    Employee("Aryan",480000),

]

managers = [
    Managers("DS", 1000000),
    Managers("Manav", 100000),
    Managers("Apoorv", 100000)
]

for e in employees:
    print(e.get_info())

for m in managers:
    print(m.get_info())


# here we will still learn abour the shaopes using oops concepts:

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @abstractmethod
    def render(self):
        pass

class Circle(shape):
    def render(self):
        return f" the x and y of circle is {self.x} and {self.y}"
    
class Rectangle(shape):
    def render(self):
        return f"the x and y of the rectangle is {self.x} and {self.y}"
    
class Square(shape):
    pass
    
shapes =[
    Circle(30, 40),
    Rectangle(100, 20),
    shape(50,50),
    Square(60, 60)
]

for s in shapes:
    print(s.render())

