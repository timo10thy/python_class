class calc:
    def add(self, a,b):
        return a+b
    def subtract(self, a,b):
        return a-b
    def multiply(self, a,b):
        return a*b
    def division(self, a,b):
        if b == 0:
            return "opps: Division by zero"
        return a/b
calculation = calc()
add_total =calculation.add(2,3)
print(add_total)
subtract_total = calculation.subtract(4,3)
print(subtract_total)
product = calculation.multiply(2,3)
print(product)
divide = calculation.division(2,2)
print(divide)
