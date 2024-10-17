from lector import readln
from __init__ import biblioteca
from gestor import Gestor

class Menu:
    @staticmethod
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

    @staticmethod
    def menu():
        while True:
            Menu.mostrar_menu()
            opcio = str(readln.scintpos('> '))
            
            if opcio == "1":
                if Gestor.afegir_llibre():
                    print("Llibre afegit correctament.")
                else: print("Error: No s'ha pogut afegir el llibre.")

            elif opcio == "2":
                if Gestor.afegir_pelicula():
                    print("Pel·lícula afegida correctament.")
                else: print("Error: No s'ha pogut afegir la pel·lícula.")

            elif opcio == "3":
                if Gestor.afegir_revista():
                    print("Revista afegida correctament.")
                else: print("Error: No s'ha pogut afegir la revista.")

            elif opcio == "4":
                if Gestor.afegir_soci():
                    print("Soci afegit correctament.")
                else: print("Error: No s'ha pogut afegir el soci.")

            elif opcio == "5":
                if Gestor.afegir_administrador():
                    print("Administrador afegit correctament.")
                else: print("Error: No s'ha pogut afegir l'administrador.")

            elif opcio == "6":
                print("Prestar un recurs a un soci")
                if Gestor.asignarMaterial():
                    print("Assignat correctament.")
                else: print("Error: No s'ha pogut assignar.")
            elif opcio == "7":
                print("Retornar un recurs")
                if Gestor.retornarMaterial():
                    print("Retornat correctament.")
                else: print("Error: No s'ha pogut retorar.")
                
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
                print(biblioteca.str_societats())

            elif opcio == "12":
                print("Eixint de l'aplicació...")
                break
            else:
                print("Opció no vàlida. Intenta-ho de nou.")


