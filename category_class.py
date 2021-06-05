class Category: 


    def __init__(self, category, amount): #different objects of the class
        self.category = category
        self.amount = amount 
    
    def deposit(self):
        amount_d= int(input("how much would you like to deposit:\n"))
        self.amount += amount_d
        print('\n Amount Deposited:', amount_d)

            
    def check_balance(self, amount_d):
        print("your current balance is:", amount_d)
        

    def withdraw(self):
        amount_w= int(input("how much would you like to withdraw:\n"))
        self.amount += amount_w
        print('\n Amount withdrew:', amount_w)
        

    def transfer(self): 
        amount_t = int(input('Transfer Amount:\n'))
        self.amount += amount_t
        print("\n Amount transfered")




class Clothing(Category):

    def __init__(self, category, amount):
        super().__init__(category, amount)
        


class Entertainment(Category):
    def __init__(self, category, amount):
        super().__init__(category, amount)
        pass



class Food(Category):
    def __init__(self, category, amount):
        super().__init__(category, amount)
        pass






x = Clothing(Clothing,500)

x.deposit()
        
# category_1 = Category("Clothing", 1000) # this is an instacne of an object
# category_2 = Category("Entertainment", 1000)
# category_3 = Category("Food", 1000)
# category_4 = Category("Streaming TV", 1000)