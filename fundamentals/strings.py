name = 'ahmadraza'
age = 22

#Concatenate 
print ('I am ' + name + 'and I am ' + str(age))

#String formating

#Arguments by position
print('I am {name} and I am {age} ' .format(name=name, age=age))

#F-strings

print(f'I am {name} and I am {age}')

#string methods
print(name.capitalize())
#make all upper case
print(name.upper())
#make all lower
print(name.lower())
#swap case
print(name.swapcase())
#Get len
print(len(name))
#replace
print(name.replace('raza','hassan'))
#count
sub= 'h'
print(name.count(sub))
#Start with
print(name.startswith('ahmad'))
#Ends with
print(name.endswith('hello'))
#split into a list
print(name.split())
# Find position
print(name.find('d'))

#is all alphanumeric
print(name.isalnum())
#is all alpha
print(name.isalpha())

#is all numeric
a='565784'
print(a.isnumeric())
