name = "Ahmad "
age = 22
languages = ['javascript', 'python', 'c++']

for lang in languages:
    print(f'My name is {name}. And I love {lang}.')


def greetings(name,age):
   return f'My name is {name} and I am {age}'

print(greetings('Ahmad Raza', 22))

data = {'name':'Ahmad', 'prof':'Programmer', 'age':'22'}
print(f'My name is ' + data['name'] + '. And I am a ' + data['prof'] + ' And i am ' + data['age'] + ' years old.' )

