import re   #regular expression
from linia import Linia
from rectangle import Rectangle
import config
class Manager:

    def __add_figura(figura):
        config.Dibuix["Figures"].apend(figura)
        pass

    def upload_figura():
        pass

    def export_svgfigura():
        pass

    def dibuixar_figura():
        pass


    def afegir_l_r(dades, tipo):
        dades = dades.split()
        if Manager.__comprovaHEX(color):
            if tipo == "l":
                x1 = int(dades[0])
                y1 = int(dades[1])
                x2 = int(dades[2])
                y2 = int(dades[3])
                color = dades[4]
                figura = Linia(x1, y1, x2, y2, color)
            elif tipo == "r":
                x1 = int(dades[0])
                y1 = int(dades[1])
                x2 = int(dades[2])
                y2 = int(dades[3])
                color = dades[4]
                figura = Rectangle(x1, y1, x2, y2, color)
            elif tipo == "c":
                #TODO
                pass

            Manager.__add_figura(figura)


    def __comprovaHEX(hex_string):
        match =re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_string)
        if match:
            return True
        else:
            return False
    
    def regex_l_r(expresio):
        match =re.search(r'^(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', expresio)
        if match:
            return True
        else:
            return False

    def regex_c(expresio):
        match =re.search(r'^(\d+)\s+(\d+)\s+([+-]?\d*\.?\d+)\s+#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', expresio)
        if match:
            return True
        else:
            return False
