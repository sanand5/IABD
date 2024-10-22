from punt import Punt
from figura import Figura
from rectangle import Rectangle
from cercle import Cercle
from linia import Linia
from menu import Menu
from manager import Manager

if __name__ == "__main__":
    p1=Punt(2,3)
    p2=Punt(3,7)
    color="#34FFDF"
    f=Figura(p1,color)
    print(f)

    l=Linia(p1,p2,color)
    print(l)
    print("La longitud es",l.perimetre())

    r=Rectangle(p1,p2,color)
    print(r)
    print("El perímetre es",r.perimetre())
    print("El area es",r.area())

    c=Cercle(p1,4,color)
    print(c)
    print("El perímetre es",c.perimetre())
    print("El area es",c.area())