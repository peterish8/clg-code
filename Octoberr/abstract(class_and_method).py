'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def voice():
        pass
class dog(Animal):
    def voice(self):
        print("Bark")
class Lion(Animal):
    def voice(self):
        print("Roar")
obj1 = dog()
obj1.voice()
obj2 = Lion()
obj2.voice()
'''






# payment (abstract),creditcard,cash,upi (are the classes) , the 
# payment method is in payment class, (abstract method)
# user calls any func in creditcard,cash,upi it shld print its respcetive amount (which is private data)
# let user give input


#using getter method

from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount
    
    @abstractmethod
    def payment_method(self):
        pass

class CreditCard(Payment):
    def payment_method(self):
        print("Credit Card Payment:", self.get_amount())

class Cash(Payment):
    def payment_method(self):
        print("Cash Payment:", self.get_amount())

class UPI(Payment):
    def payment_method(self):
        print("UPI Payment:", self.get_amount())

choice = input("Choose payment(1,2,3): ")
a = int(input("Enter the amount: "))

if choice == "1":
    payment = CreditCard(a)
elif choice == "2":
    payment = Cash(a)
elif choice == "3":
    payment = UPI(a)
    
payment.payment_method()





# Name mangling (attribute) way

from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount
    @abstractmethod
    def payment_method(self):
        pass

class CreditCard(Payment):
    def payment_method(self):
        print("Credit Card Payment:", self._Payment__amount) # these (self._Payment__amount) is name mangling

class Cash(Payment):
    def payment_method(self):
        print("Cash Payment:", self._Payment__amount)  # these (self._Payment__amount) is name mangling

class UPI(Payment):
    def payment_method(self):
        print("UPI Payment:", self._Payment__amount)  # these (self._Payment__amount) is name mangling

choice = input("Choose payment(1,2,3): ")
a = int(input("Enter the amount: "))

if choice == "1":
    payment = CreditCard(a)
elif choice == "2":
    payment = Cash(a)
elif choice == "3":
    payment = UPI(a)
    
payment.payment_method()









