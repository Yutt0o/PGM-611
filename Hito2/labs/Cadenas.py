class math_utils:
    app = ''
    version = ''
    year = ''
    ci = ''

    def __init__(self, app, version, year,ci):
        self.app = app
        self.version = version
        self.year = year
        self.ci = ci
    
    def getapp(self):
        return self.app
    
    def getci(self):
        return self.ci

    def setversion(self, version):
        self.version =  version
        
    def setyear(self, year):
        self.year =  year

    def printmath(self):
        print("APP:", self.app, self.version, self.year,self.ci)
        
    def naturalnumerio(self,numb):
        i = 1
        result = ''
        while i <= numb:
            result = result + str(i) + ' '
            i = i + 1
        print("Resultado:", result)
        
    def imparlo(self,numb):
        result = ''
        for i in range(1,numb+1,2):
            result = result + str(i) + ' '
        print("Resultado:", result)

