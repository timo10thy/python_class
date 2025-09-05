class InventoryStorage:
    def __init__(self):
        self.items ={}
    def add_item(self, items_name, quantity):
        if items_name not in self.items:
            self.items[items_name] =  quantity
        else:
            self.items[items_name] +=quantity
    def remove_items(self, items_name):
        if items_name  in self.items:
            del self.items[items_name]
        else:
            print(f"{items_name} not available")
    def update_stock(self, items_name, quantity):
        self.items[items_name] = quantity
    def show_inventory(self):
        return self.items
'''
store = InventoryStorage()
print(store.items)
store.add_item("apple",2)
store.add_item("apple",2)
print(store.items)
'''
treasure_store = InventoryStorage()
favour_store = InventoryStorage()
treasure_store.add_item("apple",2)
print("treasure store:",treasure_store.items)
favour_store.add_item("pinapple", 3)
print("favour store:",favour_store.items)
favour_store.remove_items("pinapple")
print("favour store : after removing",favour_store.items)
favour_store.update_stock("pinapple", 5)
print("favour store : after updating",favour_store.items)
print("Treasure Store Inventory:", treasure_store.show_inventory())
print("Favour Store Inventory:", favour_store.show_inventory())