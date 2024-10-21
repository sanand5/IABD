import math

class Punt:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def dist(self, altre):
        return math.sqrt((altre.x - self.x)**2 + (altre.y - self.y)**2)
    
    def dist_x(self, altre):
        return abs(self.x - altre.x)

    def dist_y(self, altre):
        return abs(self.y - altre.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, altre):
        return self.x == altre.x and self.y == altre.y
    
if __name__ == "__main__":
    p1 = Punt(0, 0)
    p2 = Punt(3, 4)
    
    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")
    print(f"Distancia entre p1 y p2: {p1.dist(p2)}")
    print(f"Distancia en el eje x entre p1 y p2: {p1.dist_x(p2)}")
    print(f"Distancia en el eje y entre p1 y p2: {p1.dist_y(p2)}")
    print(f"¿Son los puntos iguales? {p1 == p2}")