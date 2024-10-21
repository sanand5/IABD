from punt import Punt
from abc import ABC, abstractmethod
from manager import Manager

class Figura:
    def __init__(self, punt_inicial, color):
        self._punt_inicial = punt_inicial
        self._color = color
        
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetre(self):
        pass
    
    def __str__(self):
        return f"Figura: {self.__class__.__name__}, Punt inicial: {self.punt_inicial}, Color: {self.color}"

if __name__ == "__main__":
        p1=Punt(2,3)
        p2=Punt(3,4)
        color="#34FFDF"
        print (f'El color {color} valid={Manager.comprovaHEX(color)}')
        f=Figura(p1,color)
        print(f)