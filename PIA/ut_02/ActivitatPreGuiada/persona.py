class Persona:
    def __init__(self, nom, dni, id):
        self._nom = nom
        self._dni = dni
        self.id = id
    

    def getnom(self):
        return self._nom
    def getdni(self):
        return self._dni
    def getid(self):
        return self.id
    def setnom(self, nou_nom):
        self._nom = nou_nom
    def setdni(self, nou_dni):
        self._dni = nou_dni
    def __str__(self):
        return f"Nom: {self._nom}, DNI: {self._dni}"

class Soci(Persona):
    
    def __init__(self, nom, dni, id):
        super().__init__(nom, dni, id)
        self._materials = []

    def add_material(self, llibre):
        self._materials.append(llibre)
    def remove_material(self, llibre):
        self._materials.remove(llibre)
    def get_llibres(self):
        return self._materials
    def __str__(self):
        return super().__str__() + f", Llibres: {[str(l) for l in self._materials]}"

class Administrador(Persona):
    def __init__(self, nom, dni, carrec, id):
        super().__init__(nom, dni, id)
        self._carrec = carrec
    
    def getcarrec(self):
        return self._carrec
    def setcarrec(self, nou_carrec):
        self._carrec = nou_carrec
    def __str__(self):
        return super().__str__() + f", Càrrec: {self._carrec}"