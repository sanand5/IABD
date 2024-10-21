from figura import Figura
class Rectangle(Figura):
    def __init__(self, altre):
        super().__init__()
        self.altre = altre

    def area(self):
        return self.altre[0][0] * self.altre[1][0] - self.altre[0][1] * self.altre[1][1]
    
    def perimetre(self):
        return 2 * (abs(self.altre[0][0] - self.altre[1][0]) + abs(self.altre[0][1] - self.altre[1][1]))
    