
# create:
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
         print(f'My name is {self.name} and I am {self.age}')
    
    def has_birthday(self):
        self.age +=1
 # init user object
brad = User('Ahmad raza', 'ahmad@gmail.com', 22 )  

print(type(brad))
print(brad.name)

brad.has_birthday()

print(brad.greeting())