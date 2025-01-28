import time


# Create "MenuItem" class holding served drinks, their prices and ingredients
class MenuItem:
    # Initialize an instance with 3 attributes: name, price and ingredients
    def __init__(self,name,price,**kargs):
        self.name = name
        self.price = price
        self.ingredients = kargs
        
    # Dunder function for printing MenuItem
    def __repr__(self):
        prompt = f"Drink: {self.name}\nPrice: ${self.price}\n" + "Recipe:\n\t" + \
         "\n\t".join([f"{ingredient}:{amount}" for ingredient, amount in self.ingredients.items()])

        return prompt





# Create "Menu" class holding instances of "MenuItem"s
class Menu:
    # Constructor: Initialize an instance with specified "MenuItem"s
    def __init__(self,*args:MenuItem):
        """
        Parameters: MenuItems
        
        """
        menu = dict()     
        for item in args:
            menu[item.name] = item      
        self.menu = menu    
        

    # Method: Get all names of drinks existing in the Menu in a concatenated string
    def get_items(self):
        return '/'.join([menu_item.name for menu_item in self.menu.values()])

        


    # Method: Searches through the menu for the drink with specified name, return a MenuItem object if exists
    def find_drink(self,order_name:str):
        """
        Parameters: name of the order
        Return: MenuItem Object or False
        """
        return self.menu.get(order_name,False)






# Create "CoffeeMachine" class for processing orders input by a user
class CoffeeMachine:
    # Initialize an instance with starting resources given by input
    def __init__(self,**kargs):
        self.ingredients = kargs

        self.rev = 0

    def __repr__(self):
        return "Coffee Machine:\n\t" + \
            "\n\t".join([f"{ingredient}:{amount}"
                          for ingredient,amount 
                          in self.ingredients.items()]) + \
            "\n\t" + f"Revenue:${self.rev}"   

    # Method for checking if resources left is enough for making the order
    def is_sufficient_resource(self,order_item:MenuItem):
        """
        Function for checking if Coffee Machine holds enough resources for the drink
        Parameters:
          drink: MenuItem Object for the specified drink
        """
        for ingredient,amount in order_item.ingredients.items():
            if self.ingredients.get(ingredient,0) < amount:
                return False
        
        return True      



    # Method for making the order, depleting the corresponding resources
    def make_cofffee(self,order_item:MenuItem):
        for ingredient,amount in order_item.ingredients.items():
            self.ingredients[ingredient] -= amount
        
        self.rev += order_item.price

        time.sleep(5)

        
        


# Create a class for processing payment, setting currency system
class MoneyMachine():
    def __init__(self,**kwargs):
        #initializing with name of coins and their face values, in terms of ratio to a dollar
        self.coins = kwargs
    
    def get_coins(self):
        #string representation of coin machine, displaying names of the coins and their face values
        return '/'.join(self.coins.keys())
    


    def is_sufficient_payment(self,payment_dict:dict,order_item:MenuItem):
        total = 0
        for coin, n_coins in payment_dict.items():
            total += self.coins[coin] * n_coins

        return total >= order_item.price, round(total,2)






if __name__ == "__main__":

    # Create a menu
    menu = Menu(
        MenuItem("Espresso",
                 1.5,
                 water=50,
                 coffee=18),
        MenuItem("Latte",
                 2.5,
                 water=200,
                 coffee=24,
                 milk=150),
        MenuItem("Cappuccino",
                 3.0,
                 water=200,
                 coffee=24,
                 milk=100)

    )

    
    # Starting a Coffee Machine with a certain amount of resources
    cm = CoffeeMachine(water=500, milk=300, coffee=100)


    # Starting a Money Machine to process payments
    mm = MoneyMachine(cent=1/100, nikel=1/20, dime=1/10, quarter=1/4)

    is_on = True

    while is_on:
        user_input = input(
            f"""
            Hi there, fancy a cup of coffee? You can order {menu.get_items()} on this machine, 
                to order, type the name of the drink
                to check the price and ingredients of the drink, type 'Menu'
            What would you like to do?☕
            """
        )

        if user_input == "off":
            is_on = False
        elif user_input == "report":
            print(cm)
        elif user_input == "Menu":
            for drink in menu.menu.values(): 
                print(drink)
        elif user_input in menu.get_items().split("/"):
            print(f"please insert your coins, {mm.get_coins()} are accepted 💰,type 'Menu' to check the menu again")

            order = menu.find_drink(user_input)
            
            if not cm.is_sufficient_resource(order):
                print("Resource not enough for the order, please choose another one😁")
            else:
                payment_sufficient = False

                while not payment_sufficient:
                    payment_dict = dict()
                    for coin in mm.coins.keys():
                        money_input = str()
                        while not money_input.isdigit():
                            money_input = input(f"How many {coin}s?")
                            if money_input == "Menu":
                                for drink in menu.menu.values(): 
                                    print(drink)
                            elif money_input == "off":
                                is_on = False
                                break

                        if not is_on:
                            break
                        payment_dict[coin] = int(money_input)


                    if not is_on:
                            break
                    
                    money_check_bool,total = mm.is_sufficient_payment(payment_dict=payment_dict,order_item=order)
                    
                    if money_check_bool:
                        print(f"Payment accepted, here's your change of ${total - order.price}")
                        payment_sufficient = True
                    else:
                        print(f"Insufficient payment, you've paid ${total}, but {order.name} costs ${order.price}")

                if not is_on:
                        break
                
                print("Preparing your order...")
                cm.make_cofffee(order)
                print(f"Voila, your {order.name} is ready, enjoy!")
                










    

