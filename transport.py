class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) >= self.capacity:
            return "Bus is full"
        if name in self.passengers:
            return f"{name} exist"
        else:
            self.passengers.append(name)
            return f"{name} added successfully"

    def remove_passenger(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
        else:
            return f"no passenger with such {name}"

    def show_passengers(self):
        return self.passengers

metro_bus = Bus(capacity=3)
print(metro_bus.add_passenger("John"))
print(metro_bus.add_passenger("Mary"))
print(metro_bus.add_passenger("Paul"))
print(metro_bus.add_passenger("Lisa"))  

print(metro_bus.show_passengers())  
