class Material:
    def __init__(self, titol, cantitat):
        self._titol = titol
        self._cantitat = cantitat
    

    def gettitol(self):
        return self.titol
    def getcantitat(self):
        return self.cantitat
    def settitol(self, nou_titol):
        self.titol = nou_titol
    def setcantitat(self, nova_cantitat):
        self.cantitat = nova_cantitat
    def __str__(self):
        return f"Material: {self.titol}, Cantitat: {self.cantitat}"

class Llibre(Material):
    def __init__(self, titol, cantitat, autor):
        super().__init__(titol, cantitat)
        self._autor = autor
    
    def getautor(self):
        return self.autor
    def setautor(self, nou_autor):
        self.autor = nou_autor
    def __str__(self):
        return super().__str__() + f", Autor: {self.autor}"
    
class Revista(Material):
    def __init__(self, titol, cantitat, data_publicacio):
        super().__init__(titol, cantitat)
        self._data_publicacio = data_publicacio
    
    def getData_publicacio(self):
        return self.data_publicacio
    def setData_publicacio(self, nova_data_publicacio):
        self.data_publicacio = nova_data_publicacio
    def __str__(self):
        return super().__str__() + f", Data Publicació: {self.data_publicacio}"
    
class Pelicula(Material):
    def __init__(self, titol, cantitat, director, genere):
        super().__init__(titol, cantitat)
        self._director = director
        self._genere = genere
    
    def getdirector(self):
        return self.director
    def setdirector(self, nou_director):
        self.director = nou_director
    def getgenere(self):
        return self.genere
    def setgenere(self, nou_genere):
        self.genere = nou_genere
    def __str__(self):
        return super().__str__() + f", Director: {self.director}, Gènere: {self.genere}"

class Persona:
    def __init__(self, nom, dni):
        self._nom = nom
        self._dni = dni
    
    def getnom(self):
        return self._nom
    def getdni(self):
        return self._dni
    def setnom(self, nou_nom):
        self._nom = nou_nom
    def setdni(self, nou_dni):
        self._dni = nou_dni
    def __str__(self):
        return f"Persona: {self.nom}, DNI: {self.dni}"

class Soci(Persona):
    def __init__(self, nom, dni, llibres):
        super().__init__(nom, dni)
        self._llibres = []
    
    def add_llibre(self, llibre):
        self._llibres.append(llibre)
    def remove_llibre(self, llibre):
        self._llibres.remove(llibre)
    def get_llibres(self):
        return self._llibres
    def __str__(self):
        return super().__str__() + f", Llibres: {[str(l) for l in self._llibres]}"

class Administrador(Persona):
    def __init__(self, nom, dni, carrec):
        super().__init__(nom, dni)
        self._carrec = carrec
    
    def getcarrec(self):
        return self._carrec
    def setcarrec(self, nou_carrec):
        self._carrec = nou_carrec
    def __str__(self):
        return super().__str__() + f", Càrrec: {self._carrec}"
    