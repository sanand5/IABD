from materials import *

class Biblioteca:
    ids =  set()
    def __init__(self):
        self._materials = []
        self._societats = []
        self._administradors = []
    
    def asignar_id(self):
        if Biblioteca.ids:
            id_material = max(Biblioteca.ids) + 1
        else:
            id_material = 1
        Biblioteca.ids.add(id_material)
        return id_material

    def add_llibre(self, llibre):
        self._materials.append(llibre)  

    def add_revista(self, revista):
        self._materials.append(revista)

    def add_pelicula(self, pelicula):
        self._materials.append(pelicula)

    def add_soci(self, soci):
        self._societats.append(soci)
    
    def add_administrador(self, administrador):
        self._administradors.append(administrador)

    def str_llibres(self):
        return "Llibres:" + "\n" + "\n".join([str(l) for l in self._materials if isinstance(l, Llibre)])

    def str_revistes(self):
        return "Revistes:"+ "\n" + "\n".join([str(r) for r in self._materials if isinstance(r, Revista)])

    def str_pelicules(self):
        return "Películes:"+ "\n"+"\n".join([str(p) for p in self._materials if isinstance(p, Pelicula)])

    def str_societats(self):
        return "Socis:"+ "\n" +"\n".join([str(s) for s in self._societats])

    def str_administradors(self):
        return "Administradors:"+ "\n"+"\n".join([str(a) for a in self._administradors])

    def str_materials(self):
        return self.str_llibres() + "\n" + self.str_revistes() + "\n" + self.str_pelicules()