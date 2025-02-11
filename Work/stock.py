class Stock:


    def __init__(self, name:str, shares:int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self)->float:
        return self.shares * self.price  
    
    def sell(self, amount:int)-> int:
        self.shares -= amount
        return self.shares 

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor
    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()
    

