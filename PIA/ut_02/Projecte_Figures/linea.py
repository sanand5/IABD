from figura import Figura

class Linea(Figura):
    def __init__(self, altre):
        self.altre = altre

    def area(self):
        return 0
    def perimetre(self):
        return self.altre.distancia(self.altre)
    
