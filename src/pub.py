class Pub:
    def __init__(self, name, till):
        self.name = name
        self.drinks = []
        self.till = till
        self.drinks_sold = 0
        
        
    def add_drink(self, drink):
        self.drinks.append(drink)    


    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink   
    

    def add_to_till(self, amount):
        self.till += amount


    def remove_customer_cash(self, amount, customer):
        self.pub.customer.wallet -= amount


        
        

        
    


    # def sell_drink(self, drink, customer):
    #     drink = self.find_drink_by_name(drink) 
    #  increase till money --->  add_to_till
    #
    # reduce customer money  ---> remove_money(amount, customer)