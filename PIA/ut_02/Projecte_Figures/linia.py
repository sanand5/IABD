from figura import Figura

class Linia(Figura):
    def __init__(self, p1, p2, color):
        super().__init__(p1, color)
        self._altre = p2
    

    @property
    def altre(self):
        return self._altre

    @altre.setter
    def altre(self, value):
        self._altre = value

    def area(self):
        return 0
    def perimetre(self):
        return super().punt_inicial.dist(self.altre)
    
    def __str__(self):
        return f"Figura: {self.__class__.__name__}, Punt inicial: {self.punt_inicial}, Altre: {self.altre}, Color: {self.color}"
    
