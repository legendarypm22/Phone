class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __call__(self, phoneNumber):
        print(f"{self.brand} is calling")

    def __str__(self) -> str:
        return f"Brand{self.brand}Price = {self.price}"


iphone = Phone("Iphone 7+", 300)
samsung = Phone("Samsung s20", 300)
print(iphone.brand)
print(samsung.price)












