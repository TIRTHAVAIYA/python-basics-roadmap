### CLASS METHOD & STATIC METHOD

class Pizza:
    base_price = 650

    def __init__(self,toppings):
        self.toppings = toppings


    @classmethod
    def pepperoni(cls):
        return cls(['pepperoni' , 'cheese'])
    
    @staticmethod

    def is_vegetarian(toppings):
        return not any (meat in toppings for meat in ['prpperoni' , 'sausage' , 'ham'])
    
    def get_details(self):
        veg_status = "Vegetarian" if self.is_vegetarian(self.toppings) else "Non-Vegetarian"
        return f"Toppings: {','.join(self.toppings)}.Status:{veg_status}"


## CREATING INSTANCE....

pepperoni_pizza = Pizza.pepperoni()
print("Factory Method Used : ")
print(f"Is a simple cheese pizza veg??{Pizza.is_vegetarian(['cheese'])}")

veg_pizza = Pizza(['mushrooms' , 'olives'])
print(veg_pizza.get_details())
