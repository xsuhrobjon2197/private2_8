class Protuct:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        
    def info(self):
        print(f"nomi = {self.name}, narxi = {self.price}")
        
    
p1 = Protuct("Olma", 10000)
p2 = Protuct("Uzum", 15000)
p3 = Protuct("Anjir", 22000)
p4 = Protuct("Anor", 27000)

print(p1.name)

roy = [p1, p2, p3, p4]
print(roy[0].name)
print(roy[0].price)
