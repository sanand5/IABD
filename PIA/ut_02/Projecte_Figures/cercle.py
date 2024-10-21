from figura import Figura

class Cercle(Figura):
    def __init__(self, radi):
        super().__init__()
        self._radi = radi
    
    def area(self):
        return 3.14 * self.radi ** 2
    
    def perimetro(self):
        return 2 * 3.14 * self.radi