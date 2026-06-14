people = ['Ahmad', 'raza', 'hassan', 'aqsa']

# for loop

for person in people:
    print(f'Current Person: {person}')


# break

for person in people:
    if person == 'raza':
     break
    print(f'Current Person: {person}')

#continue

for person in people:
    if person == 'raza':
     continue
    print(f'Current Person: {person}')

    #range

    for i in range(len(people)):
       print(people[i])


for i in range(0,11):
 print(i)


 #while loops

 count = 0
while count <= 10:
 print(f'Count: {count}')
 count += 1
