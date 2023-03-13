import csv
from datetime import datetime 
#importing the required libraries


class Pizza:

    def __init__(self, description, cost): #initializing the class
        self.description = description #description of the pizza
        self.cost = cost #cost of the pizza

    def get_description(self):
        return self.description #getter for encapsulation

    def get_cost(self):
        return self.cost #getter for encapsulation


class ClassicPizza(Pizza):

    def __init__(self):
        super().__init__("Classic Pizza", 119.90)

class MargheritaPizza(Pizza):

    def __init__(self):
        super().__init__("Margherita Pizza", 106.90)

class TurkPizza(Pizza):
    
    def __init__(self):
        super().__init__("Turkish Pizza", 149.90)

class PlainPizza(Pizza):
    
    def __init__(self):
        super().__init__("Plain Pizza", 99.90)


class Decorator(Pizza):

    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.component.get_description() + " with " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_saucecost(self):
        return self.cost
    
    def get_saucedescription(self):
        return self.description


class Olives(Decorator):
    
    def __init__(self, component):
        super().__init__(component, "Olives", 4.90)

class Mushrooms(Decorator):

    def __init__(self, component):
        super().__init__(component, "Mushrooms", 4.90)

class GoatCheese(Decorator):
        
    def __init__(self, component):
        super().__init__(component, "Goat Cheese", 12.90)

class Meat(Decorator):

    def __init__(self, component):
        super().__init__(component, "Meat", 14.90)

class Onions(Decorator):
        
    def __init__(self, component):
        super().__init__(component, "Onions", 4.90)    

class Corn(Decorator):

    def __init__(self, component):
        super().__init__(component, "Corn", 4.90)

def isValidID(id_number):
    id_number = str(id_number) #converting the id number to string

    if not len(id_number) == 11: #checking if the id number is 11 digits 
        return False
    
    if not id_number.isdigit(): #checking if the id number containing only digits
        return False

    if int(id_number[0]) == 0: #checking if the id number starts with 0
        return False
    
    digits = [int(x) for x in id_number] #converting the id number to a list of digits	

    if not sum(digits[:10]) % 10 == digits[10]: #checking if the 
        return False
    
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]: #
        return False

    return True

def isValidCreditCardNumber(cc_number): #checking if the credit card number is valid with luhn algorithm

    ndigits = len(cc_number)
    nsum = 0
    isSecond = False

    for i in range(ndigits - 1, -1, -1):
        d = ord(cc_number[i]) - ord('0')

        if(isSecond == True):
            d = d * 2

        nsum += d // 10
        nsum += d % 10

        isSecond = not isSecond

    if (nsum % 10 == 0):
        return True
    else:
        return False


def main():

     #opening the csv file in read mode

    file = open("menu.txt", "w") #opening the file in write mode

    menu_text = """
    Please Choose a Pizza Base: 
    1: Classic Pizza 119.90 ₺
    2: Margherita Pizza 106.90 ₺
    3: Turkish Pizza 149.90 ₺
    4: Plain Pizza 99.90 ₺
    * and sauce of your choice: 
    11: Olives +4.90 ₺
    12: Mushrooms +4.90 ₺
    13: Goat Cheese +12.90 ₺
    14: Meat +14.90 ₺
    15: Onions +4.90 ₺
    16: Corn +4.90 ₺
    * Thank you!!
    """

    file.write(menu_text) #writing the menu to the file
    file.close()#closing the file

    print(menu_text)#printing the menu to the console

    

    while(True):
        pizza_type = int(input("Please choose a pizza base: ")) #getting the pizza type from the user
        if pizza_type == 1:
            pizza = ClassicPizza() 
            break
        elif pizza_type == 2:
            pizza = MargheritaPizza()
            break
        elif pizza_type == 3:
            pizza = TurkPizza()
            break
        elif pizza_type == 4:
            pizza = PlainPizza()
            break
        else:
            print("Invalid choice!")

    savep = pizza #saving the pizza for the receipt	

    while(True):
        sauce_type = int(input("Please choose a sauce: ")) #getting the sauce type from the user
        if sauce_type == 11:
            pizza = Olives(pizza) #adding the sauce to the pizza
            break
        elif sauce_type == 12:
            pizza = Mushrooms(pizza)
            break
        elif sauce_type == 13:
            pizza = GoatCheese(pizza)
            break
        elif sauce_type == 14:
            pizza = Meat(pizza)
            break
        elif sauce_type == 15:
            pizza = Onions(pizza)
            break
        elif sauce_type == 16:
            pizza = Corn(pizza)
            break
        else:
            print("Invalid choice!")
    
    
    name = input("Please enter your name: ") #getting the name from the user

    id_number = input("Please enter your ID number: ") #getting the id number from the user

    while(True):
        if isValidID(id_number): #checking if the id number is valid
            break
        else:
            print("Invalid ID Number!")
            id_number = input("Please enter your ID number: ")

    print("\nHere is your receipt:") #printing the receipt
    print(savep.get_description() + " " + f"{savep.get_cost():.2f} ₺") #printing the pizza base and its cost
    print(pizza.get_saucedescription() + " " + f"{pizza.get_saucecost():.2f} ₺") #printing the sauce and its cost
    print("----------------------------------")
    print("Total Cost: " + f"{pizza.get_cost():.2f} ₺") #printing the total cost

    found = False

    with open("Orders_Database.csv", "a+") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
          print(row)
          if row[1] == id_number:
              found = True
              credit_card_number = row[2]
              credit_card_password = row[6]
              break

        if found:
            print("Do you want to use your previous credit card information? (Y/N)")
            choice = input()
            if choice == "Y" or "y":
                pass
            elif choice == "N" or "n":
                credit_card_number = input("Please enter your credit card number: ")
                while(True):
                    if isValidCreditCardNumber(credit_card_number):
                        break
                    else:
                        print("Invalid Credit Card Number!")
                        credit_card_number = input("Please enter your credit card number: ")
                credit_card_password = input("Please enter your credit card password: ")

        else:
            credit_card_number = input("Please enter your credit card number: ")
            while(True):
                if isValidCreditCardNumber(credit_card_number):
                    break
                else:
                    print("Invalid Credit Card Number!")
                    credit_card_number = input("Please enter your credit card number: ")
            credit_card_password = input("Please enter your credit card password: ")



    

        
            
    
        
            
     #getting the choice from the user
     #getting the credit card number from the user	
    
    
    description = pizza.get_description()
    cost = pizza.get_cost()

    now = datetime.now() #getting the current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S") #formatting the date and time


    with open("Orders_Database.csv", "a+") as csvfile: #opening the csv file in append mode
        writer = csv.writer(csvfile) #creating a csv writer object
        writer.writerow([name, id_number, credit_card_number, description, cost, date_time, credit_card_password]) #writing the order to the csv file
    
    print("\nThank you for your order!")
    print("\nOrder Details:")
    print("Name: " + name)
    print("ID Number: " + id_number)
    print("Order: " + description)
    print(f"Cost: {cost:.2f} ₺")
    print("Date: " + date_time)
    print("Order saved to database!") 



        

if __name__ == "__main__":
    main()
