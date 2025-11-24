'''
# single inheritance
# if a single class has one parent class.
class teacher:
    def show(self):
        print("hello")
class student(teacher):
    def visible(self):
        print("hey")
obj1 = student()
obj1.visible()
obj1.show()



# multiple inheritance
# if a single class has multiple parent class.

class teacher:
    def show(self):
        print("hello")
class professor():
    def lecture(self):
        print("bye")
class student(teacher,professor):
    def visible(self):
        print("hey")
obj1 = student()
obj1.visible()
obj1.show()
obj1.lecture()



# multi-level inheritance
# means a class inherits from a class that itself inherits from another class — forming a chain.
#👴 Grandparent class → 🧑 Parent class → 👶 Child class

class Teacher:
    def show(self):
        print("hello")

class Professor(Teacher):  # Inherits from Teacher
    def lecture(self):
        print("bye")

class Student(Professor):  # Inherits from Professor
    def visible(self):
        print("hey")

class Kid(Student):  # Inherits from Student
    def play(self):
        print("play") 

obj2 = Kid()
obj2.play()      # Output: play
obj2.visible()   # Output: hey
obj2.lecture()   # Output: bye
obj2.show()      # Output: hello





# Hierarchical Inheritance
# Hierarchical inheritance means multiple child classes inherit from the same parent class.
# One parent class with Many child classes that share its traits

class Teacher:
    def show(self):
        print("hello")

class Student1(Teacher):  # Inherits from Teacher
    def visible(self):
        print("hey from Student1")

class Student2(Teacher):  # Also inherits from Teacher
    def visible(self):
        print("hey from Student2")

class Student3(Teacher):  # Also inherits from Teacher
    def visible(self):
        print("hey from Student3")

obj1 = Student1()
obj2 = Student2()
obj3 = Student3()

obj1.show()      # Inherited from Teacher
obj1.visible()   # Defined in Student1

obj2.show()      # Inherited from Teacher
obj2.visible()   # Defined in Student2

obj3.show()      # Inherited from Teacher
obj3.visible()   # Defined in Student3


# Hybrid inheritance
# Hybrid inheritance is a combination of two or more types of inheritance in a single program
# building a family tree with branches that include grandparents, siblings, and cousins 
# all connected in different ways

class Teacher:
    def show(self):
        print("Hello from Teacher")

class Student1(Teacher):
    def visible(self):
        print("Hey from Student1")

class Student2(Teacher):
    def visible(self):
        print("Hey from Student2")

class Student3(Teacher):
    def visible(self):
        print("Hey from Student3")

# Hybrid class inheriting from multiple students
class Coordinator(Student1, Student2):
    def visible(self):
        print("Hey from Coordinator")

obj = Coordinator()
obj.show()      # Inherited from Teacher via Student1
obj.visible()   # Only Coordinator's visible() is called



'''

'''
class carparent:
    def __init__(self,model,fuel,color):
        self.model = model
        self.fuel = fuel
        self.color = color
        print(self.model,self.fuel,self.color)
class carchild(carparent):
    def __init__(self,model,fuel,color,engine):
        super().__init__(model,fuel,color)
        self.model = model
        self.fuel = fuel
        self.color = color
        self.engine = engine
        print(self.model,self.fuel,self.color,self.engine)
obj1 = carchild("top",50,"black",2000)

'''


class university:
    def __init__(self):
        self.attendance = int(input("Enter your attendance: "))
        self.marks = int(input("Enter your marks: "))

class college(university):
    def __init__(self):
        super().__init__()
    def eligible(self):
        return self.attendance > 75
    def result(self):
        return self.marks > 30

class school(college):
    def __init__(self):
        super().__init__() 
    def check_status(self):
        if self.eligible():  
            print("You are eligible")
        else:
            print("You are not eligible")
        if self.result(): 
            if self.marks == 100: 
                print("Your Raksha")
            else:
                print("ur pass")
        else:
            print("You failed")

obj = school()
obj.check_status()




        

