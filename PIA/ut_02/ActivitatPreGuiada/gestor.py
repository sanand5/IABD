from lector import readln
from __init__ import Biblioteca, biblioteca
from materials import Llibre, Pelicula, Revista
from persona import  Soci, Administrador

class Gestor:
    
    @staticmethod
    def afegir_llibre():
        print("Afegir un nou llibre")
        titol = readln.scstr("Títol: ")
        cantitat = readln.scintpos("Cantitat: ")
        autor = readln.scstr("Autor: ")
        biblioteca.add_llibre(Llibre(titol, cantitat, autor, biblioteca.asignar_id()))
        return True
    
    @staticmethod
    def afegir_pelicula():
        print("Afegir una nova pel·lícula")
        titol = readln.scstr("Títol: ")
        cantitat = readln.scintpos("Cantitat: ")
        director = readln.scstr("Director: ")
        genere = readln.scstr("Gènere: ")
        biblioteca.add_pelicula(Pelicula(titol, cantitat, director, genere, biblioteca.asignar_id()))
        return True

    @staticmethod
    def afegir_revista():
        # TODO: Comprobar data
        print("Afegir una nova revista")
        titol = readln.scstr("Títol: ")
        cantitat = readln.scintpos("Cantitat: ")
        data_publicacio = readln.scstr("Data de publicació (dd/mm/yyyy): ")
        biblioteca.add_revista(Revista(titol, cantitat, data_publicacio, biblioteca.asignar_id()))
        return True

    @staticmethod
    def afegir_soci():
        # TODO: Comprobar DNI
        print("Afegir un nou soci")
        nom = readln.scstr("Nom: ")
        dni = readln.scstr("DNI: ")
        biblioteca.add_soci(Soci(nom, dni, biblioteca.asignar_id()))
        return True
    
    @staticmethod
    def afegir_administrador():
        # TODO: Comprobar DNI
        print("Afegir un nou administrador")
        nom = readln.scstr("Nom: ")
        dni = readln.scstr("DNI: ")
        carrec = readln.scstr("Càrrec (administrador / ajudant / exit): ").lower()
        # TODO: While per a tornar a preguntar
        if carrec == 'administrador' or carrec == 'ajudant':
            biblioteca.add_administrador(Administrador(nom, dni, carrec, biblioteca.asignar_id()))
            return True
        else: return False 

    @staticmethod
    def buscar_soci(dni):
        for soci in biblioteca._societats:
            if soci.getdni() == dni:
                return soci
        return False

    @staticmethod
    def buscar_material(idmaterial):
        for material in biblioteca._materials:
            if material.getid() == idmaterial:
                return material
        return False

    @staticmethod
    def asignarMaterial():
        print(Biblioteca.str_materials())
        material = readln.scstr("Disme id del recurs que vols prestar: ")
        if Gestor.buscar_material(material)!= False: 
            print(Biblioteca.str_societats())
            soci = readln.scstr("Disme el DNI del soci: ")
            if Gestor.buscar_soci(soci) != False: 
                soci.add_material(material)
            else: 
                print("Error: No s'ha trobat el soci.")
                return False
        else: 
            print("Error: No s'ha trobat el recurs.")
            return False
        return True
    
    @staticmethod
    def retornarMaterial():
        print(Biblioteca.str_materials())
        soci = readln.scstr("Disme el DNI del soci: ")
        if Gestor.buscar_soci(soci) != False: 
            print(soci)
            material = readln.scstr("Disme id del recurs que vols tornar: ")
            if Gestor.buscar_material(material)!= False:
                soci.remove_material(material)
            else: 
                print("Error: No s'ha trobat el recurs.")
                return False
        else: 
            print("Error: No s'ha trobat el soci.")
            return False


