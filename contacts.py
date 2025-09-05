class ContactBook:
    def __init__(self):
        self.contact ={}
    def add_items(self, name,number):
        if name not in self.contact:
            self.contact[name] = number
            return f"{name} added successfuly"
        else:
            return f"{name} exist"
    def remove_contact(self,name):
        if name in self.contact:
            del self.contact[name]
            return f"{name} deleted successfully"
        else:
            return f"{name} does not exit"
    def search(self, name):
        if name in self.contact:
            return f"{name} {self.contact[name]}"
        else:
            return f"{name} not found"
    def show_contact(self):
        return self.contact

book = ContactBook()
print(book.add_items("alice",674646464))
print(book.add_items("mimi",674646464))
print(book.add_items("tom",674646464))
print(book.remove_contact("alice"))
print(book.search("tim"))
print(book.search("tom"))
print(book.show_contact())