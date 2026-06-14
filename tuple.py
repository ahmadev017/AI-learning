
# a tuple is a built-in data type used to store an 
# ordered collection of items, similar to a list — but 
# with one key difference: tuples are immutable 
# (cannot be changed after creation).

#create tuple
fruits=('Apples', 'Oranges',  'Grapes')


#destructuring
#fruits2 =tuple(('Apples', 'Oranges',  'Grapes')) 


#single value needs trailing comma
fruits2=('Apples',)

#get value
print(fruits[1])


#cant change value
 #fruits[0] = 'pears'

# del tuple
del fruits2

#get length

print(len(fruits))

#print(fruits2, type(fruits2))

#print(fruits, fruits2)



#Unlike lists and tuples, sets:

#❌ Do not allow duplicates
#❌ Do not maintain order
#✅ Are mutable (you can add/remove items)
#✅ Are very fast for searching


fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# check if in set

print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')


# cant add duplicate

fruits_set.add('Apples')

print(fruits_set)

#Remove from set

fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()


#delete set
del fruits_set

#print(fruits_set)