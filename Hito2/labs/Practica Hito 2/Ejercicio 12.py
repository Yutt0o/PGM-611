class Person:
    name = None
    email = None
    gender = None
    nationality = None
    
    def __init__(self,name, email, gender, nationality):
        self.name = name
        self.email = email
        self.gender = gender
        self.nationality = nationality
        
    def __str__(self):
        return f'Name: {self.name} \nEmail: {self.email} \nGender: {self.gender} \nNationality: {self.nationality} \n'
    
    def Write_book(self):
        pass
    def Write_a_movies(self):
        pass
    
    def change_nationality(self, newnationality):
        self.nationality = newnationality
        
    def change_email(self, newemail):
        self.email = newemail

per1 = Person('William','asdk@gmail.com', 'Masculine', "Bolivian")
print(per1)


per1.change_nationality('Mexican')
per1.change_email('dfgk@gmail.com')
print(per1)