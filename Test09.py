class Laptop:
    clas_vr = 100
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
    
    def greet(self, name):
        print(f"Hello, {name}!, Thanks for shopping.")
        
    @classmethod
    def cls_method_example(cls):
        cls.clas_vr = 1000     
        print(f"Class variable: {cls.clas_vr}")


prema_laptop = Laptop(50000, 59)
print(prema_laptop.price)
print(prema_laptop.weight)
print(Laptop.clas_vr)
prema_laptop.greet("Bobi")
Laptop.cls_method_example()


vicky_lap = Laptop(60000, 67)
print(vicky_lap.price)
print(vicky_lap.weight)
print(Laptop.clas_vr)



        