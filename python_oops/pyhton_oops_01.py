# class Employee:
#     def __init__(self, name, salary ):
#         self.name = name
#         self.salary = salary


# e1 = Employee("Apoorv", 36000)
# e2 = Employee("Rohan", 36000)
# e3 = Employee("Aryan", 48000)

# print(e1.name, e1.salary)
# print(e2.name, e2.salary)
# print(e3.name, e3.salary)


#2nd code: 


# class Employee:
#     def __init__(self, First_name, Last_name, Salary):
#         self.First_name = First_name
#         self.Last_name = Last_name
#         self.Salary = Salary

#     def get_full_name(self):
#         return(f"the name and salary is {self.First_name} {self.Last_name} and it is {self.Salary}")
            
# e1 = Employee("Apoorv", "Pandey", 36000)
# e2 = Employee("Rohan", "Dixit", 36000)
# e3 = Employee("Aryan", "Kumar", 48000)


# print(e1.get_full_name())
# print(e2.get_full_name())
# print(e3.get_full_name())

#3rd code: 

class Employee:
    def __init__(self, First_name, Last_name, Salary):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Salary = Salary

    def get_full_name(self):
        return(f"the name and salary is {self.First_name} {self.Last_name} and it is {self.Salary}")
    
    def raise_salary(self, percentage):
        self.Salary = self.Salary * (100 + percentage)/100

    def add_bonus(self, amount):
        self.Salary = self.Salary + amount

            
e1 = Employee("Apoorv", "Pandey", 36000)
e2 = Employee("Rohan", "Dixit", 36000)
e3 = Employee("Aryan", "Kumar", 48000)


print(e1.get_full_name())
print(e2.get_full_name())
print(e3.get_full_name())

e1.raise_salary(10)
e2.raise_salary(10)
e3.raise_salary(10)

print("here are ther updated salaries of the of the eployees")

print(f"Updated salary of the employee e1 = {e1.Salary}" )
print(f"Updated salary of the employee e1 = {e2.Salary}")
print(f"Updated salary of the employee e1 = {e3.Salary}")


print("here is the updated salary with raised bonus")

e1.add_bonus(10000)
e2.add_bonus(10000)
e3.add_bonus(10000)

print(f"{e1.Salary}")
print(f"{e2.Salary}")
print(f"{e3.Salary}")

