

class Menu: 

    def mostrar_principal():
        print("""
            Indica el que vols fer:
            1 - Afegir figura al dibuix
            2 - Carregar dibuix des de fitxer
            3 - Exportar  dibuix a SVG
            4 - Dibuixar i exir
            """)
        
    def menu_principal():
        Menu.mostrar_principal() 
        opcio = int(input("Opció: "))
        while True:
            if opcio == 1:
                
                break
            elif opcio == 2:
                
                break
            elif opcio == 3:
                
                break
            elif opcio == 4:
                
                break
            else:
                print("Opció no valida. Torna a intentar-ho.")
                opcio = int(input("Opció: "))

    def mostrar_figura():
        print("""
            Indica la figura que vols afegir:
            1 - Linia
            Introdueix les dades de la linia (x1 y1 x2 y2 #color):
            2 - Rectangle
            Introdueix les dades de la Rectangle (x1 y1 x2 y2 #color): 
            3 - Cercle
            Introdueix les dades de la Cercle (x1 y1 r #color):
            """)
        
    def menu_figura():
        Menu.mostrar_figura() 
        opcio = input("Opció: ")
        #TODO: Logica per a saber quina figura s'ha seleccionat i llegir les dades necessaries per crear-la



            
    
        