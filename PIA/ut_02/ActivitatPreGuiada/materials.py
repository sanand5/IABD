class Material:
    def __init__(self, titol, cantitat, id):
        self._titol = titol
        self._cantitat = cantitat
        self.id = id

    def gettitol(self):
        return self.titol
    def getcantitat(self):
        return self.cantitat
    def getid(self):
        return self.id
    def settitol(self, nou_titol):
        self.titol = nou_titol
    def setcantitat(self, nova_cantitat):
        self.cantitat = nova_cantitat
    def __str__(self):
        return f"Títol: {self._titol}, Cantitat: {self._cantitat}, ID: {self.id}  "

class Llibre(Material):
    def __init__(self, titol, cantitat, autor, id):
        super().__init__(titol, cantitat, id)
        self._autor = autor
    
    def getautor(self):
        return self._autor
    def setautor(self, nou_autor):
        self._autor = nou_autor
    def __str__(self):
        return super().__str__() + f", Autor: {self._autor}"
    
class Revista(Material):
    def __init__(self, titol, cantitat, data_publicacio, id):
        super().__init__(titol, cantitat, id)
        self._data_publicacio = data_publicacio

    def getData_publicacio(self):
        return self.data_publicacio
    def setData_publicacio(self, nova_data_publicacio):
        self.data_publicacio = nova_data_publicacio
    def __str__(self):
        return super().__str__() + f", Data Publicació: {self._data_publicacio}"
    
class Pelicula(Material):
    def __init__(self, titol, cantitat, director, genere, id):
        super().__init__(titol, cantitat, id)
        self._director = director
        self._genere = genere

    def getdirector(self):
        return self._director
    def setdirector(self, nou_director):
        self._director = nou_director
    def getgenere(self):
        return self._genere
    def setgenere(self, nou_genere):
        self._genere = nou_genere
    def __str__(self):
        return super().__str__() + f", Director: {self._director}, Gènere: {self._genere}"