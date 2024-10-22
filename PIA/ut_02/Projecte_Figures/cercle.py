from figura import Figura

class Cercle(Figura):
    def __init__(self, p1, radi, color):
        super().__init__(p1, color)
        self._radi = radi
    
    @property
    def radi(self):
        return self._radi
    @radi.setter
    def radi(self, value):
        self._radi = value

    def area(self):
        return 3.14 * self.radi ** 2
    
    def perimetre(self):
        return 2 * 3.14 * self.radi
    
    def __str__(self):
        return f"Figura: {self.__class__.__name__}, Punt inicial: {self.punt_inicial}, Radi: {self.radi}, Color: {self.color}"