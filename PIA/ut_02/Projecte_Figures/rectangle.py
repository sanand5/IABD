from figura import Figura
class Rectangle(Figura):
    def __init__(self, p1,p2,color):
        super().__init__(p1,color)
        self._altre = p2
        self.__longitud = abs(self.altre.x - super().punt_inicial.x)
        self.__altura = abs(self.altre.y - super().punt_inicial.y)

    @property
    def altre(self):
        return self._altre
    @altre.setter
    def altre(self, value):
        self._altre = value
    @property
    def longitud(self):
        return self.__longitud
    @property
    def altura(self):
        return self.__altura

    def area(self):
        return self.longitud * self.altura
    
    def perimetre(self):
        return 2 * (self.longitud + self.altura)
    
    def __str__(self):
        return f"Figura: {self.__class__.__name__}, Punt inicial: {self.punt_inicial}, Altre: {self.altre}, Color: {self.color}"    
    