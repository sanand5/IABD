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
        return f"Títol: {self._titol}, Cantitat: {self._cantitat}"

class Llibre(Material):
    def __init__(self, titol, cantitat, autor):
        super().__init__(titol, cantitat)
        self._autor = autor
    
    def getautor(self):
        return self._autor
    def setautor(self, nou_autor):
        self._autor = nou_autor
    def __str__(self):
        return super().__str__() + f", Autor: {self._autor}"
    
class Revista(Material):
    def __init__(self, titol, cantitat, data_publicacio):
        super().__init__(titol, cantitat)
        self._data_publicacio = data_publicacio
    
    def getData_publicacio(self):
        return self.data_publicacio
    def setData_publicacio(self, nova_data_publicacio):
        self.data_publicacio = nova_data_publicacio
    def __str__(self):
        return super().__str__() + f", Data Publicació: {self._data_publicacio}"
    
class Pelicula(Material):
    def __init__(self, titol, cantitat, director, genere):
        super().__init__(titol, cantitat)
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
        return f"Nom: {self._nom}, DNI: {self._dni}"

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

class Biblioteca:
    def __init__(self):
        self._materials = []
        self._societats = []
        self._administradors = []

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

class readln:

    def scstr(msg):
        return input(msg)
    
    def scint(msg):
        while True:
            try:
                num = readln.rdint(msg)
                return num
            except ValueError:
                print("Error: el número ha de ser un número enter.")
        
    def rdint(msg):
        return int(input(msg))
    
    def scintpos(msg):
        num = readln.scint(msg)
        while num <= 0:
            print("Error: el número ha de ser positiu.")
            num = readln.scint(msg)
        return num
    
def afegir_llibre():
    print("Afegir un nou llibre")
    titol = readln.scstr("Títol: ")
    cantitat = readln.scintpos("Cantitat: ")
    autor = readln.scstr("Autor: ")
    biblioteca.add_llibre(Llibre(titol, cantitat, autor))
    return True

def afegir_pelicula():
    print("Afegir una nova pel·lícula")
    titol = readln.scstr("Títol: ")
    cantitat = readln.scintpos("Cantitat: ")
    director = readln.scstr("Director: ")
    genere = readln.scstr("Gènere: ")
    biblioteca.add_pelicula(Pelicula(titol, cantitat, director, genere))
    return True

def afegir_revista():
    # TODO: Comprobar data
    print("Afegir una nova revista")
    titol = readln.scstr("Títol: ")
    cantitat = readln.scintpos("Cantitat: ")
    data_publicacio = readln.scstr("Data de publicació (dd/mm/yyyy): ")
    biblioteca.add_revista(Revista(titol, cantitat, data_publicacio))
    return True

def afegir_soci():
    # TODO: Comprobar DNI
    print("Afegir un nou soci")
    nom = readln.scstr("Nom: ")
    dni = readln.scstr("DNI: ")
    biblioteca.add_soci(Soci(nom, dni, []))
    return True

def afegir_administrador():
    # TODO: Comprobar DNI
    print("Afegir un nou administrador")
    nom = readln.scstr("Nom: ")
    dni = readln.scstr("DNI: ")
    carrec = readln.scstr("Càrrec (administrador / ajudant / exit): ").lower()
    # TODO: While per a tornar a preguntar
    if carrec == 'administrador' or carrec == 'ajudant':
        biblioteca.add_administrador(Administrador(nom, dni, carrec))
        return True
    else: return False 


def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓ DE BIBLIOTECA ---")
    print("1. Afegir llibre")
    print("2. Afegir pel·lícula")
    print("3. Afegir revista")
    print("4. Afegir soci")
    print("5. Afegir administrador de préstecs")
    print("6. Prestar un recurs a un soci")
    print("7. Retornar un llibre")
    print("8. Mostrar llista de recursos (llibres, pel·lícules, revistes)")
    print("9. Mostrar llista de socis")
    print("10. Mostrar llista d'administradors de préstecs")
    print("11. Mostrar recursos prestats per cada soci")
    print("12. Eixir")
    print("-------------------------------------")

def menu():
    while True:
        mostrar_menu()
        opcio = str(readln.scintpos('> '))
        
        if opcio == "1":
            if afegir_llibre():
                print("Llibre afegit correctament.")
            else: print("Error: No s'ha pogut afegir el llibre.")

        elif opcio == "2":
            if afegir_pelicula():
                print("Pel·lícula afegida correctament.")
            else: print("Error: No s'ha pogut afegir la pel·lícula.")

        elif opcio == "3":
            if afegir_revista():
                print("Revista afegida correctament.")
            else: print("Error: No s'ha pogut afegir la revista.")

        elif opcio == "4":
            if afegir_soci():
                print("Soci afegit correctament.")
            else: print("Error: No s'ha pogut afegir el soci.")

        elif opcio == "5":
            if afegir_administrador():
                print("Administrador afegit correctament.")
            else: print("Error: No s'ha pogut afegir l'administrador.")

        elif opcio == "6":
            print("Prestar un recurs a un soci")

        elif opcio == "7":
            print("Retornar un llibre")
            
        elif opcio == "8":
            print("Mostrar llista de recursos")
            print(biblioteca.str_materials())

        elif opcio == "9":
            print("Mostrar llista de socis")
            print(biblioteca.str_societats())

        elif opcio == "10":
            print("Mostrar llista d'administradors")
            print(biblioteca.str_administradors())

        elif opcio == "11":
            print("Mostrar recursos prestats per cada soci")

        elif opcio == "12":

            print("Eixint de l'aplicació...")
            break
        else:
            print("Opció no vàlida. Intenta-ho de nou.")

biblioteca = Biblioteca()
menu()

