class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices    
        self.items = {}        

    def add_items(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        return f"{item_name} added successfully"

    def remove_items(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]
            return f"{item_name} removed successfully"
        else: 
            return f"{item_name} not in cart"

    def clear_cart(self):
        self.items = {}
        return "Cart cleared"

    def calculate_total(self):
        total = 0
        for item, qty in self.items.items():
            if item in self.prices:  
                total += self.prices[item] * qty
        return total


# Example usage
prices = {"Shirt": 5000, "Shoes": 12000}
cart = ShoppingCart(prices)

print(cart.add_items("Shirt", 2))       
print(cart.items)                       
print(cart.calculate_total())           

print(cart.remove_items("Shirt", 1))    
print(cart.items)                       
print(cart.calculate_total())  
