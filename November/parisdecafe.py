import mysql.connector as m
import sys

con = m.connect(host="localhost",user="root",password="root")
cur = con.cursor()

cur.execute("create database if not exists paris_de_cafe")
cur.execute("use paris_de_cafe")

cur.execute("create table if not exists customer(customer_id int primary key, customer_name varchar(225), customer_password varchar(225))")
cur.execute("create table if not exists perks_pass(customer_id int primary key, perks_pass_balance float(8,2))")
cur.execute("create table if not exists employee(emp_id int primary key, emp_type_id int, emp_name varchar(225), emp_salary varchar(225))")
cur.execute("create table if not exists admin(admin_id int primary key, admin_name varchar(225), admin_password varchar(225))")
cur.execute("create table if not exists franzy_menu(food_id int primary key, food_name varchar(225), food_description varchar(1024), food_price int)")
cur.execute("create table if not exists food_style(food_id int primary key, food_style_id int, food_style_name varchar(225), food_style_description varchar(1024), food_style_price int)")
cur.execute("create table if not exists orders(order_id int primary key, order_name varchar(225), order_description varchar(1024), order_price int)")
cur.execute("create table if not exists cart(customer_id int,food_id int, adding_price int)")

print("-"*90)
print("                   🥐| PARIS_DE_CAFE |🥐                  ")
print("-"*90)
print("........................Start your day with something sweet and warm..........................")
print("........................... ^_^ start your order right away ^_^ .........................")

admin_id = None
cashier_id = None
customer_id = None

def main_menu():
  while True:
    print("1. customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))
    print()
    if choice == 1:
      askcustomer()
    elif choice == 2:
      admin_login()
    elif choice == 3:
      print("😀thanks our visiting our paris cafe!!😀")
      break
    else:
      print("Invalid choice. Please try again.😌")

def askcustomer():
  while True:
    print("1. Login Here!")
    print("2. New To Paris de Café? (Create an Account!)")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
      ch = 1
      customer_login()
      break
    elif choice == 2:
      ch = 1
      create_account_customer()
      break
    elif choice == 3:
      print("back to main menu")
      break
    else:
      print("Invalid choice. Please try again.😶")

def create_account_customer():
  while True:
    global customer_id
    customer_id = int(input("Enter your customer ID: "))
    customer_name = input("Enter your username: ")
    customer_password = input("Enter your password: ")
    cur.execute("select * from customer")
    data = cur.fetchall()
    for i in data:
      if i[0] == int(customer_id):
        print("this Id has been already opted. please try a different Id.")
        break
      elif i[1] == customer_name:
        print("This username is already taken. Please style a different username.")
        break
      else:
        print("this account is good to go now!")
        break
    cur.execute("insert into customer values(%s,%s,%s)",(customer_id, customer_name, customer_password))
    cur.execute("insert into perks_pass values(%s,%s)",(customer_id, 1000.0))
    con.commit()
    print("Account created successfully!🎊")
    break

def customer_login():
  while True:
    global customer_id
    customer_id = int(input("Enter your customer ID: "))
    customer_name = input("Enter your username: ")
    customer_password = input("Enter your password: ")
    cur.execute("select * from customer")
    data = cur.fetchall()
    login_success = False
    for i in data:
      if i[0] == customer_id and i[2] == customer_password:
        print("Welcome customer:", i[1])
        customer_menu()
        login_success = True
        break
    if not login_success:
      print("Invalid customer ID. Please try to login again.")
    else:
      break

def customer_menu():
  while True:
    global customer_id
    print("🍺^^^^^Welcome to Paris de Café online service^^^^^!!🍺")
    print("1. franzy_menu")
    print("2. Food Stye-Based menu")
    print("3. Cart")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
      print("franzy_menu:")
      cur.execute("select * from franzy_menu")
      data = cur.fetchall()
      for i in data:
        print("Food ID:",i[0],"Food name:",i[1],"Food description:",i[2],"Food price:",i[3])
      print("1. Add to cart")
      print("2. Exit")
      choice = int(input("Enter your choice (1-2): "))
      if choice == 1:
        while True:
          food_id = int(input("Enter the food ID: "))
          cur.execute("select * from franzy_menu where food_id = %s",(food_id,))
          data = cur.fetchall()
          for i in data:
            print("Food ID:",i[0],"Food name:",i[1],"Food price:",i[3])
          cur.execute("insert into cart values(%s,%s,%s)",(customer_id,i[0],i[3]))
          print("1. continue shopping")
          print("2. go to cart")
          print("3. exit")
          choice = int(input("Enter your choice (1-3): "))
          if choice == 1:
            continue
          elif choice == 2:
            cur.execute("select * from cart where customer_id = %s",(customer_id,))
            data = cur.fetchall()
            for i in data:
              print("Food ID:",i[1],"Food price:",i[2])
            total = 0
            for i in data:
              total += i[2]
            print("Total price:",total)
            break
          elif choice == 3:
            break
          else:
            print("Invalid choice. Please try again.")
      elif choice==2:
        print("exited")
      else:
        print("invalid")
    elif choice == 2:
      print("Food Stye-Based menu")
      print("1. simply Strasbourg: ")
      print("2. classical Carcassonne: ")
      print("3. modernish Marseille: ")
      choice = int(input("Enter your choice (1-3): "))
      if choice == 1:
        while True:
          print("~~~ simply Strasbourg ~~~")
          cur.execute("select * from food_style where food_style_id = 1")
          data = cur.fetchall()
          for i in data:
            print("Food name:",i[2],"Food description:",i[3],"Food price:",i[4])
          print("well it is a combo that you chose, its price reduces 10 percentage from its original price.")
          cur.execute("select * from food_style where food_style_id = 1")
          data = cur.fetchall()
          print("1. Add to cart")
          print("2. Exit")
          choice = int(input("Enter your choice (1-2): "))
          if choice == 1:
            cur.execute("select * from food_style where food_style_id = 1")
            data = cur.fetchall()
            for i in data:
              cur.execute("insert into cart values(%s,%s,%s)",(customer_id,i[0],i[4]-i[4]*0.10))
              con.commit()
            print("Added to cart")
            break
          elif choice == 2:
            print("back to main menu")
            break
      elif choice == 2:
        while True:
          print("~~~ classical Carcassonne ~~~")
          cur.execute("select * from food_style where food_style_id = 2")
          data = cur.fetchall()
          for i in data:
            print("Food name:",i[2],"Food description:",i[3],"Food price:",i[4])
          print("well it is a combo that you chose, its price reduces 10 percentage from its original price.")
          cur.execute("select * from food_style where food_style_id = 2")
          data = cur.fetchall()
          print("1. Add to cart")
          print("2. Exit")
          choice = int(input("Enter your choice (1-2): "))
          if choice == 1:
            cur.execute("select * from food_style where food_style_id = 2")
            data1 = cur.fetchall()
            for i in data1:
              cur.execute("insert into cart values(%s,%s,%s)",(customer_id,i[0],i[4]-i[4]*0.10))
              con.commit()
            print("Added to cart")
            break
          elif choice == 2:
            print("back to main menu")
            break
      elif choice == 3:
        while True:
          print("~~~ modernish Marseille ~~~")
          cur.execute("select * from food_style where food_style_id = 3")
          data2 = cur.fetchall()
          for i in data2:
            print("Food name:",i[2],"Food description:",i[3],"Food price:",i[4])
          print("well it is a combo that you chose, its price reduces 10 percentage from its original price.")
          cur.execute("select * from food_style where food_style_id = 3")
          data = cur.fetchall()
          print("1. Add to cart")
          print("2. Exit")
          choice = int(input("Enter your choice (1-2): "))
          if choice == 1:
            cur.execute("select * from food_style where food_style_id = 3")
            data3 = cur.fetchall()
            for i in data3:
              cur.execute("insert into cart values(%s,%s,%s)",(customer_id,i[0],i[4]-i[4]*0.10))
              con.commit()
            print("Added to cart")
            break
          elif choice == 2:
            print("back to main menu")
            break
      elif choice==4:
        print("you have been exited successfully")
        break
      else:
        print("invalid choice")
    elif choice == 3:
      print("1. Display Cart")
      print("2. Remove Cart")
      print("3. Clear all cart")
      print("4. Checkout")
      print("5. Exit")
      choice = int(input("Enter your choice (1-4): "))
      if choice == 1:
        cur.execute("select * from cart where customer_id = %s",(customer_id,))
        data = cur.fetchall()
        total_price = 0
        for i in data:
          print("Food name:",i[1],"Food price:",i[2])
        for i in data:
          total_price += i[2]
        print("Total price:",total_price)
      elif choice == 2:
        food_id = int(input("Enter the food ID you want to remove: "))
        cur.execute("delete from cart where food_id = %s",(food_id,))
        con.commit()
        print("food ID:",food_id,"Removed from cart")
      elif choice == 3:
        cur.execute("delete from cart where customer_id = %s",(customer_id,))
        con.commit()
        print("Cart cleared")
      elif choice == 4:
        checkout()
        cur.execute("delete from cart where customer_id = %s",(customer_id,))
        con.commit()
        break
    elif choice == 3:
      print("back to main menu")
    elif choice == 4:
      print("exited")
    else:
      print("Invalid choice. Please try again.")
      break

def admin_login():
  global Admin_id
  Admin_id = int(input("Enter your Admin ID: "))
  Admin_name = input("Enter your username: ")
  Admin_password = input("Enter your password: ")
  cur.execute("select * from admin")
  data = cur.fetchall()
  for i in data:
    if i[0] == int(Admin_id) and i[2] == Admin_password :
      print("Welcome Admin:",i[1])
      Admin_menu()
      return
    else:
      print("Invalid Admin ID. Please try to login again.")

def Admin_menu():
  print("Welcome to Paris de Café !!")
  print("1. employee")
  print("2. customer")
  print("3. Exit")
  choice = int(input("Enter your choice (1-3): "))
  if choice == 1:
    while True:
      print("1. add employee")
      print("2. remove employee")
      print("3. update employee")
      print("4. view employee")
      print("5. search employee")
      print("6. exit")
      choice1 = int(input("Enter your choice (1-6): "))
      if choice1 == 1:
        while True:
          emp_id = int(input("Enter employee ID: "))
          emp_type_id = int(input("Enter employee type ID: "))
          emp_name = input("Enter employee name: ")
          emp_salary = input("Enter employee salary: ")
          cur.execute("insert into employee values(%s,%s,%s,%s)",(emp_id,emp_type_id,emp_name,emp_salary))
          con.commit()
          print("Employee added successfully!")
          break
      elif choice1 == 2:
        while True:
          emp_id = int(input("Enter employee ID: "))
          cur.execute("delete from employee where emp_id = %s",(emp_id,))
          con.commit()
          print("Employee deleted successfully!")
          break
      elif choice1 == 3:
        while True:
          emp_id = int(input("Enter employee ID: "))
          emp_salary = int(input("Enter employee to update their salary: "))
          cur.execute("update employee set emp_salary =%s where emp_id =%s",(emp_salary,emp_id))
          con.commit()
          print("Employee updated successfully!")
          break
      elif choice1 == 4:
        while True:
          cur.execute("select*from employee")
          data = cur.fetchall()
          for i in data:
            print(i)
          break
      elif choice1 == 5:
        while True:
          emp_id = int(input("Enter employee ID: "))
          cur.execute("select*from employee where emp_id = %s",(emp_id,))
          data = cur.fetchone()
          if data:
            print(data)
          else:
            print("Employee not found")
          break
      elif choice1 == 6:
        print("back to main menu")
        break
      else:
        print("Invalid choice. Please try again.")
  elif choice == 2:
   while True:
    print("customer")
    print("1. add customer")
    print("2. remove customer")
    print("3. update customer")
    print("4. view customer")
    print("5. search customer")
    print("6. exit")
    choice2 = int(input("Enter your choice (1-6): "))
    if choice2 == 1:
      while True:
        customer_id = int(input("Enter customer ID: "))
        customer_name = input("Enter customer name: ")
        customer_password = input("Enter customer password: ")
        cur.execute("insert into customer values(%s,%s,%s)",(customer_id, customer_name, customer_password))
        con.commit()
        print("Customer added successfully!")
        break
    elif choice2 == 2:
      while True:
        customer_id = int(input("Enter customer ID: "))
        cur.execute("delete from customer where customer_id = %s",(customer_id,))
        con.commit()
        print("Customer deleted successfully!")
        break
    elif choice2 == 3:
      while True:
        customer_id = int(input("Enter customer ID: "))
        customer_name = input("Enter customer name: ")
        customer_password = input("Enter customer password: ")
        cur.execute("update customer set customer_name = %s, customer_password = %s where customer_id = %s",(customer_name, customer_password, customer_id))
        con.commit()
        print("Customer updated successfully!")
        break
    elif choice2 == 4:
      while True:
        cur.execute("select*from customer")
        data = cur.fetchall()
        for i in data:
          print(i)
        break
    elif choice2 == 5:
      while True:
        customer_id = int(input("Enter customer ID: "))
        cur.execute("select*from customer where customer_id = %s",(customer_id,))
        data = cur.fetchone()
        if data:
          print(data)
        else:
          print("Customer not found")
        break
    elif choice2 == 6:
      print("back to main menu")
      break
    else:
      print("Invalid choice. Please try again.")
  elif choice == 3:
    print("back to main menu")
  else:
    print("Invalid choice. Please try again.")

def thanks_page():
  print("Thanks for shopping with us!")
  sys.exit()

def checkout():
  global customer_id
  print("Your cart:")
  cur.execute("select*from cart where customer_id = %s",(customer_id,))
  data = cur.fetchall()
  total_price = 0
  for i in data:
    print("Food name:",i[1],", Food price:",i[2])
    total_price += i[2]
  print("Total price:",total_price)
  cur.execute("select*from perks_pass where customer_id = %s",(customer_id,))
  data = cur.fetchone()
  print("your perks pass balance:",data[1])
  willing = int(input("enter 1 if you want to confirm the checkout / 2 for going back to the cart: "))
  if willing == 1:
    if data[1] < total_price:
      print("Insufficient balance. Please add more money to your perks pass.")
    elif data[1] >= total_price:
      cur.execute("update perks_pass set perks_pass_balance = %s where customer_id = %s",(data[1] - total_price, customer_id))
      con.commit()
      print("Checkout successful!")
      print("As you purchased a small gift from our side!")
      print("₹",total_price*0.10, "amount is added to your perks pass (10% from your purchase)")
      cur.execute("select * from perks_pass where customer_id = %s",(customer_id,))
      perk = cur.fetchone()
      print("Now your total balance in your perks pass is:",perk[1],"+",total_price*0.10,"=",perk[1]+total_price*0.10)
      cur.execute("update perks_pass set perks_pass_balance = %s where customer_id = %s",(perk[1]+total_price*0.10, customer_id))
      con.commit()
      thanks_page()

main_menu()

'''
it is been inserted in the paris_de_cafe database (mysql) , franzy_menu table

INSERT INTO franzy_menu VALUES
  (1, 'Croissant au Beurre', 'A flaky butter croissant, warm from the oven.', 325),
  (2, 'Café Crème Brûlée', 'A velvety coffee with a caramelized sugar crust.', 412),
  (3, 'Café Caramel','Caramel-flavored coffee with whipped cream.', 375),
  (4, 'Café Espresso', 'Espresso-flavored coffee with whipped cream.', 389),
  (5, 'Café Viennois', 'Espresso topped with whipped cream and cocoa.', 398),
  (6, 'Café Latte', 'Caffeinated milk coffee with whipped cream.', 398),
  (7, 'Café Frappe', 'Caffeinated milk coffee with whipped cream and ice.', 412),
  (8, 'Café Macchiato', 'Caffeinated espresso-flavored coffee with whipped cream.', 412),
  (9, 'Café Mocha', 'Caffeinated chocolate-flavored coffee with whipped cream.', 412),
  (10,'Café Cappuccino', 'Caffeinated espresso-flavored coffee with whipped cream and ice.', 412),
  (11,'Chocolat Chaud', 'Thick, decadent hot chocolate.', 321),
  (12,'Fondant au Chocolat', 'A rich chocolatey fondant with whipped cream.', 345),
  (13,'Tiramisu', 'A luscious, chocolate-flavored ice cream.', 362),
  (14,'Pâté à la Mode', 'Creamy French bread with a side of crème fraîche.', 347);

it is been inserted in the paris_de_cafe database (mysql) , food_style table

INSERT INTO food_style values
  (3,1, 'Café Caramel(combo-pack)', 'Caramel-flavored coffee with whipped cream.',375),
  (13,1, 'Fondant au Chocolat(combo-pack)', 'A rich chocolatey fondant with whipped cream.',345),
  (14,1, 'Tiramisu(combo-pack)', 'A luscious, chocolate-flavored ice cream.',362),
  (1,2, 'Croissant au Beurre(combo-pack)', 'A flaky butter croissant, warm from the oven.',325),
  (2,2, 'Café Crème Brûlée(combo-pack)', 'A velvety coffee with a.creationized sugar crust.',412),
  (11,2, 'Éclair au Chocolat(combo-pack)', 'Light pastry filled with chocolate cream.',273),
  (4,3, 'Café Espresso(combo-pack)', 'Espresso-flavored coffee with whipped cream.',389),
  (12,3, 'Chocolat Chaud(combo-pack)', 'Thick, decadent hot chocolate.',321),
  (15,3, 'Pâté à la Mode(combo-pack)', 'Creamy French bread with a side of crème fraîche.', 347);

it is been inserted in the paris_de_cafe database (mysql) , admin table

insert into admin values(1,"admin","admin123");

'''