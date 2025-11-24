'''class student:
    name = ""
    roll = 0
    marks = 0
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def represent(self):
        print(self.name,self.roll)
    def passfail(self):
        if self.marks < 30:
            print("FAIL")
        else:
            print("PASS")
    
student1 = student("Prathick",18,29)
student1.represent()
student1.passfail()

st2 = student("Dhanes",12,31)
st2.represent()
st2.passfail()
'''


class employee:
    name = ""
    dept = ""
    sal= 0
    def __init__(self,name,dept,sal):
        self.name = name
        self.dept = dept
        self.sal = sal


    def represent(self):
        print(self.name,self.dept)


    def increment(self):
        if self.dept == "sales":
            a = self.sal + (self.sal*0.10)
        elif self.dept == "IT":
            a = self.sal + (self.sal*0.20)
        elif self.dept == "marketing":
            a = self.sal + (self.sal*0.25)
        else:
            print("The dept is not matching ")

        print("Your initial salary", self.sal,"Your updated salary",a)

employees = {
    "Prathick": ["marketing", 5000],
    "Dhanes": ["IT", 5000],
    "Messi": ["sales", 5000]
}

person1 = input("Enter ur name:")

if person1 in employees:
    dept, salary = employees[person1]
    person = employee(person1, dept, salary)
    person.represent()
    person.increment()
else:
    print("Employee not found in the record!")




