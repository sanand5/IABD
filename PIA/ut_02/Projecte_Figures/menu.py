from lector import readln
from manager import Manager

class Menu: 

    def __mostrar_principal():
        print("""
            Indica el que vols fer:
            1 - Afegir figura al dibuix
            2 - Carregar dibuix des de fitxer
            3 - Exportar  dibuix a SVG
            4 - Dibuixar i exir
            """)
        
    def menu_principal():
        Menu.__mostrar_principal() 
        opcio = readln.scint("Opció: ")
        while True:
            if opcio == 1:
                Menu.__menu_figura()
                break
            elif opcio == 2:
                
                break
            elif opcio == 3:
                
                break
            elif opcio == 4:
                
                break
            else:
                print("Opció no valida. Torna a intentar-ho.")
                opcio = readln.scint("Opció: ")

    def __mostrar_figura():
        print("""
            Indica la figura que vols afegir:
            1 - Linia
            2 - Rectangle
            3 - Cercle
            """)
        
    def __menu_figura():
        Menu.__mostrar_figura() 
        seguir = True
        while seguir:
            opcio = readln.scint("Opció: ")
            if opcio == 1:
                dades = readln.scstr("Introdueix les dades de la linia (x1 y1 x2 y2 #color):")
                if Manager.regex_l_r(dades):
                    Manager.afegir_l_r(dades, "l")
                    seguir = False
                else: print("Error: les dades introduides no són correctes.")
            elif opcio == 2:
                dades = readln.scstr("Introdueix les dades de la rectangle (x1 y1 x2 y2 #color):")
                if Manager.regex_l_r(dades):
                    Manager.afegir_l_r(dades, "r")
                    seguir = False
                else: print("Error: les dades introduides no són correctes.")
            elif opcio == 3:
                dades = readln.scstr("Introdueix les dades de la Cercle (x1 y1 r #color):")
                if Manager.regex_c(dades):
                    #TODO
                    seguir = False
                else: print("Error: les dades introduides no són correctes.")
            else:
                print("Opció no valida. Torna a intentar-ho.")
                seguir = True


        #TODO: Logica per a saber quina figura s'ha seleccionat i llegir les dades necessaries per crear-la



            
    
        