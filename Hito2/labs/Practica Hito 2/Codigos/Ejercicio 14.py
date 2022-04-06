class Vehicle:
    color = None
    wheels = None
    
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
    
    def __str__(self):
        return f'Color: {self.color}\n Wheels: {self.wheels}\n'
    
    def travel(self):
        pass
    
class Cars(Vehicle):
    sets = None
    engine = None
    
    def __init__(self, color, wheels, sets, engine):
        Vehicle.__init__(self, color, wheels)
        self.sets = sets
        self.engine = engine
    
    def __str__(self):
        return Vehicle.__str__(self) + f'Sets: {self.sets}\n Engine: {self.engine}\n'
    
    def start(self):
        pass
    def accelerate(self):
        pass

class Bicycles(Vehicle):
    saddles = None
    chain_drive = None
    
    def __init__(self,color, wheels, saddles, chain_drive):
        Vehicle.__init__(self, color, wheels)
        self.saddles = saddles
        self.chain_drive = chain_drive
    
    def __str__(self):
        return Vehicle.__str__(self) + f'Saddles: {self.saddles}\nChain Drive {self.chain_drive}'
    
    def start(self):
        pass
    def accelerate(self):
        pass

print('CAR')    
car1 = Cars('Red','Four', 'Five', 'Motor Wankel')
print(car1)

print('BICYCLE')
bic1 = Bicycles('Black', 'Two', 'One', 'Seven')
print(bic1)