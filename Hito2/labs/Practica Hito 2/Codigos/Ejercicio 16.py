class Person:
    name = None
    age = None
    email = None
    direction = None
    
    def __init__(self,name, age, email, direction):
        self.name = name
        self.age = age
        self.email = email
        self.direction = direction
    
    def __str__(self):
        return f'Nombre: {self.name}\nEdad: {self.age}\nCorreo: {self.email}\n'
    
    def observations (self, observation):
        self.observations = observation
        print(observation)    

class Student(Person):
    codeStudent = None
    
    def __init__(self,codeStudent, name, age, email, direction):
        Person.__init__(self, name, age, email, direction)
        self.codeStudent = codeStudent
    
    def __str__(self):
        return f'Codigo: {self.codeStudent}\n' + Person.__str__(self)
    
    
    def qualification (self, note):
        self.qualification = note
        print(note)

class dateXtra:
    info = None
    semester = None
    
    def __init__(self,info, semester):
        self.info = info
        self.semester = semester
    
    def __str__(self):
        return f'Informacion: {self.info}\nSemestre: {self.semester}'

class Manager(Person):
    codeManager = None
    department = None
    
    def __init__(self,codeManager, department, name, age, email, direction):
        Person.__init__(self, name, age, email, direction)
        self.codeManager = codeManager
        self.department = department
    
    def __str__(self):
        return f'Departamento: {self.department}\n' + Person.__str__(self)
    
    

class SM(Student, dateXtra):
    key = None
    
    def __init__(self,key, codeStudent, name, age, email, direction, info, semester):
        Student.__init__(self,codeStudent, name, age, email, direction)
        dateXtra.__init__(self,info, semester)
        self.key = key
    
    def __str__(self):
        return f'SM: {self.key}\n' + Student.__str__(self) + dateXtra.__str__(self)
    
    def observations(self, observation):
        self.observations = observation
        print(observation)



mn1 = Manager('Cod-001', 'Turismo', 'William', 32, 'willi@gmail.com', 'Av.Civica')
print(mn1)

st1 = Student('SIS13298376', 'Freddy', 25, 'fred@gmail.com', 'Av.Argelia')
print(st1)

sm1 = SM('SIS-TRM', 'SIS13298376', 'Vania', 18, 'vangrihs@gmail.com', 'Av. Policia', 'Sin Comentarios', 6) 
print(sm1)
