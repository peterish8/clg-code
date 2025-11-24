'''
# Method 1: Method Overriding (Original)
class Animal:
    def voice(self):
        print("Animal makes a sound")
class Cat(Animal):
    def voice(self):
        print("meow meow")
class Dog(Animal):
    def voice(self):
        print("bark bark")

dog1 = Dog()
dog1.voice()  


# Method 2: Using class attributes
class Cat4:
    sound = "meow meow"
    def voice(self):
        print(self.sound)

class Dog4:
    sound = "bark bark"
    def voice(self):
        print(self.sound)

# Testing all methods
print("Method 1:")
Cat().voice()
Dog().voice()

print("\nMethod 4:")
Cat4().voice()
Dog4().voice()

'''

class Employee:
    def calcparameter(self, a, b):
        avg = (a + b) / 2
        print("employee avg (a,b):", avg)

class Staff(Employee):
    def calcparameter(self, a, b, c, d):
        super().calcparameter(a, b)
        avg = (a + b + c + d) / 4
        print("Staff avg (a,b,c,d):", avg)
        Officer().calcparameter(a, b, c)

class Officer(Employee):
    def calcparameter(self, a, b, c):
        avg = (a + b + c) / 3
        print("officer avg (a,b,c):", avg)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

# Single call that triggers all three
Staff().calcparameter(a, b, c, d)


