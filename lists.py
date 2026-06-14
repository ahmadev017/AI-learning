#Create lists

numbers = [1,2,3,4,5,6,7]
fruits = ['oranges','mangoes', 'grapes' ]

#use a constructor

numvers2 = list ((1,2,3,4,5,6))

#Get a value
print(fruits[1])
#Get length
print(len(fruits))
#append to list 
fruits.append('apple')
#remove from list
fruits.remove('grapes')
#insert into position
fruits.insert(1, 'stawberry')
#remove with pop
fruits.pop(2)
#reverse list
fruits.reverse()
#sort list
fruits.sort()
#reverse sort
fruits.sort(reverse=True)
fruits[1] = 'Blueberry'
print(fruits)

