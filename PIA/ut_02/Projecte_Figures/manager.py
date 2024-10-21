import re   #regular expression

class Manager:

    def add_figura():
        pass

    def upload_figura():
        pass

    def export_svgfigura():
        pass

    def dibuixar_figura():
        pass

    def demanar_figura():
        pass

    def comprovaHEX(hex_string):
        match =re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_string)
        if match:
            return True
        else:
            return False
