class Copier:
    nameDoc = None
    dateDoc = None
    sheetsDoc = None
    
    def __init__(self, nameDoc, dateDoc, sheetsDoc):
        self.nameDoc = nameDoc
        self.dateDoc = dateDoc
        self.sheetsDoc = sheetsDoc
    
    def __str__(self):
        return f'Nombre del Documento: {self.nameDoc}\nFecha del Documento: {self.dateDoc}\nCantidad de Hojas: {self.sheetsDoc}\n'
    
    def senddoc(self):
        print("Documentos Enviados")

class Scanner(Copier):
    def __init__(self, nameDoc, dateDoc, sheetsDoc):
        Copier.__init__(self, nameDoc, dateDoc, sheetsDoc)
        
    def __str__(self):
        return Copier.__str__(self)

    def statusDoc(self):
        print("Documento Escaneado")

class Printer:
    def __init__(self, nameDoc, dateDoc, sheetsDoc):
        Copier.__init__(self, nameDoc, dateDoc, sheetsDoc)
        
    def __str__(self):
        return Copier.__str__(self)

    def statusDoc(self):
        print("Documento Imprimido")

class PD(Scanner, Copier):
    def __init__(self):
        print('Dispositivos Alimentados')

scaneer1 = Scanner('Proyectos', '02/03/2022', 78)
print(scaneer1)
printer1 = Printer('Hojas de Vida', '02/03/2022', 3)
print(printer1)
pd1 = PD()
pd1.statusDoc()