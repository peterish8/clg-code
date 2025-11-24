class Employee:
    def dobnow(self):
        print("Date of Birth:", self.__dob)

class NewJoinee(Employee):
    def join(self):
        print("Joining Date:", self.__joiningdate)

class Experience(NewJoinee):
    def salarytotal(self):
        print("Salary:", self.__salary)

emp = Experience()
emp._Employee__dob = "1995-08-15" 
emp._NewJoinee__joiningdate = "2022-06-01"
emp._Experience__salary = 75000

emp.dobnow()
emp.join()
emp.salarytotal()


