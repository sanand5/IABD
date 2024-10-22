class readln:

    def scstr(msg):
        return input(msg)
    
    def scint(msg):
        while True:
            try:
                num = readln.__rdint(msg)
                return num
            except ValueError:
                print("Error: el número ha de ser un número enter.")
    
    def scintpos(msg):
        num = readln.scint(msg)
        while num <= 0:
            print("Error: el número ha de ser positiu.")
            num = readln.scint(msg)
        return num
    
    def __rdint(msg):
        return int(input(msg))