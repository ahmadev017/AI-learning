#A dictionary in Python is a collection of key-value pairs.
#Think of it like a real dictionary:
#Word → Key


# create dictionary

person = {
    'first_name':'Ahmad',
    'last_name':'raza',
    'age':'22'
}
# use constructor
#person2 = dict(first_name='Sara', last_name='Williams')

#Get value
print(person['first_name'])
print(person.get('last_name'))

#add key value

person['phone'] = '634637-4783'

# Get dict keys
print(person.keys())

#get dict items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city']='RYK'
print(person2)

#Remove an item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

#Get length
print(len(person2))


#list of dict

people = [
    {
        'name':'Ahmad',
        'last_name':'raza'
    },
    {
        'name':'Ahmad2',
        'last_name':'raza2'
    }
]

print(people[1]['name'])
