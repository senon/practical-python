# stock.py
#
# Exercise 4.1
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    # Used with `repr()`
    def __repr__(self) -> str:
        return f'Stock({self.name}, {self.shares}, {self.price})'
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
    
    def panic(self):
        self.sell(self.shares)
    

