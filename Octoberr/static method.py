'''
class car:
    model = "top"
    def __init__(self,fuel_capa,color):
        self.fuel_capa = fuel_capa
        self.color= color
        print(self.color,self.fuel_capa)

    @staticmethod #this "@" thing is a decorator (decorator: takes a fun() as an input and gives fun() as an output)
    def printdetails():
        print("Hello")
obj1=car(50,"red")
car.printdetails()

'''


'''
class Animal:
    smell= "foul"
    taste="bitter"
    def __init__(self,legs,size):
        self.legs=legs
        self.size=size
    @staticmethod
    def bark():
        print("The dog is barking in sound of")
    def smell1():
        print("The dog smells foul")

    def walk(self):
        print(self.legs,self.size)
    def jump(self):
        print(self.size,self.legs)


def smelltest():
    print(self.smell)
print(smelltest())

'''



'''
#data hiding and confidentiality using __ after self, so it cant be 
class BankDetails:
    clientName = ""
    accno = 0
    bank_balance = 0
    def __init__(self,clientName,accno,bank_balance):
        self.clientName=clientName
        self.__accno=accno
        self.__bank_balance=bank_balance
obj1 = BankDetails("prats","12345","5000")
print(obj1.clientName)
print(obj1.accno)
print(obj1.bank_balance)
        
#to manipulate this private data we use setters (set)
#to see this private data we use getters (get)

'''







'''
class BankDetails:
    clientName = ""
    accno = 0
    bankbalance = 0
    def __init__(self,clientName,accno,bankbalance):
        self.clientName=clientName
        self.__accno=accno
        self.__bankbalance=bankbalance

    def setAccNo(self,accno):
        self.__accno= accno
        return self.__accno

    def getAccNo(self):
        return self.__accno
    
    def setBankBalance(self,bankbalance):
        self.__bankbalance= bankbalance
        return self.__bankbalance

    def getBankBalance(self):
        return self.__bankbalance
    def setBankBalance(self):
        return self.__bankbalance
obj1 = BankDetails("prats",12345,5000)
print(obj1.clientName)
obj1.getAccNo()
print(obj1.setAccNo(200))
obj1.getBankBalance()
print(obj1.setBankBalance(10))
'''

# name and id matching then give password field, if passowrd is matching then show bank balance
'''
class emp:
    ename = ""
    eid = 0
    epass = "heyman"
    ebalance = 5000
    def __init__(self):
        self.ename= input("Enter ur name:")
        self.eid= int(input("Enter ur id:"))
        self.__epass=emp.epass
        self.__ebalance= emp.ebalance
    
    def check1(self,ename,eid):
        if self.ename==ename and self.eid==eid:
            askpass = input("Enter ur pass:")
            if askpass==self.__epass:
                print(self.__ebalance)
            else:
                print("Password is wrong")
        else:
            print("name or id is wrong")

emp1 = emp()
emp1.check1("prats",123)

'''

d1 = {"emp1": 124, "emp2": 256, "emp3": 351}
d2 = {"emp1": "pas1", "emp2": "pas2", "emp3": "pas3"}
class EmployeeLogin:
    def __init__(self, name):
        self.name = name
        self.emp_id = None
        self.password = None
    def authenticate(self):
        if self.name not in d1:
            print("Wrong name")
            return False
        self.emp_id = int(input("Enter ID: "))
        if d1[self.name] != self.emp_id:
            print("Wrong ID")
            return False
        self.password = input("Enter password: ")
        if d2[self.name] != self.password:
            print("Wrong password")
            return False
        print("Login successful!")
        print("ID:", d1[self.name])
        return True
ask1 = input("Enter name: ")
emp = EmployeeLogin(ask1)
emp.authenticate()

