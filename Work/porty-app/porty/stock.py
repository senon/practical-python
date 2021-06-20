# stock.py
#
# Exercise 4.1
from .typedproperty import String, Integer, Float
class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
    
    @property
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
    

