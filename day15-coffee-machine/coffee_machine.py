import re
import time
class CoffeeMachine:
    #class attribute for recipe
    recipe = {
        "espresso":{
            "water":50,
            "coffee":18,
            "price":1.5
        },
        "latte":{
            "Water":200,
            "coffee":24,
            "Milk":150,
            "price":2.5
        },
        "cappuccino":{
            "Water":250,
            "coffee":24,
            "Milk":100,
            "price":3.0
        }
    }


    def __init__(self,water,milk,coffee,dollar=0):
        """
        Initializing brand new coffee machine with ingredients and amount of money specified:
        """
        self.resources = {
            "water":water,
            "milk":milk,
            "coffee":coffee
        }
        self.revenue = dollar
    

    def print_report(self):
        """
        Function for displaying current ingredients left and revenue earned in the coffee machine
        """
        print(f"""
        Water:{self.resources["water"]}ml,
        Milk:{self.resources["milk"]}ml,
        Coffee:{self.resources["coffee"]}g,
        Money:${self.revenue}
              """)
        
    def is_resource_sufficient(self,order):
        """
        Function for checking whether resources available are enough to make the order,
        return True if all ingredients are plenty, and return the name of the insufficient resource when not enough
        """
        order_recipe = self.recipe[order]

        for resource in self.resources.keys():
            if self.resources[resource] < order_recipe.get(resource,0):
                return resource
        return True        


    def receive_coins(self,n_cent,n_nikel,n_dime,n_quarter):
        """
        Function for receiving coins of different values that user has inserted and calculate the total dollar amount
        """
        return n_cent/100 + n_nikel/20 + n_dime/10 + n_quarter/4
    
    
    def prepare_order(self,order):
        """
        Function for making the order, depleting the corresponding resources and adding to the revenue
        function is called only when resource is enough for the order
        """
        order_recipe = self.recipe[order]
        for resource in self.resources.keys():
            self.resources[resource] -= order_recipe[resource]
        
        self.revenue += order_recipe["price"]



if __name__ == "__main__":
    
    #starting a new coffee machine
    cm = CoffeeMachine(1000,500,500,0)
    while True:
        user_input = input("A good day there, what would you like to order? espresso, cappuccino or latte?☕\n")
        #for maintainence, type "report" to display resource left
        if user_input == "report":
            cm.print_report()
        elif user_input in ["espresso","latte","cappuccino"]:
            resource_check = cm.is_resource_sufficient(user_input)
            #check for resource
            if resource_check == True:
                coin_input = input("Please insert your coins in the form of: xc,xn,xd,xq\n")
                dollar_input = cm.receive_coins(*(int(re.findall(r'\d+',coins)[0]) for coins in coin_input.strip().split(",")))
                
                #check if money put in is sufficient
                price = cm.recipe[user_input]["price"]
                if dollar_input < price:
                    print("Sorry, you didn't put in enough money for the order")
                else:
                    print(f"Received ${dollar_input}, here's your change of ${dollar_input - price}, order will be ready in a short while\n")
                    cm.prepare_order(user_input)
                    time.sleep(5)
                    print(f"Voilla, enjoy your {user_input}!\n")
            else:
                print(f"Sorry, there's not enough {resource_check}\n")
        #maintanence can type "off" to shut it down
        elif user_input == "off":
            break
        else:
            print("Invalid input, try reading the propmt?\n")
        
        


