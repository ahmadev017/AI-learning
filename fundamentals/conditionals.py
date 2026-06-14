
#create

x=5
y=70

if x>y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')    


#elif 
if x>y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{y} is equal to {x}')       
else:
    print(f'{y} is greater than {x}')    


#nested if 
if x > 2:
 if x <= 10:
  print(f'{x} is greater than 2 but less than 10')


#logical oprator
if x>2 and x<10:
   print(f'{x} is greater than 2 and less than 10')


# or operator

if x>2 and x<10:
   print(f'{x} is greater than 2 or less than 10')

#not

if not(x==y):
   print(f'{x} is not equal to {y}')

#Membership operators are used to check whether a value exists inside a sequence like list,string, tuple, set

numbers = [1,2,3,4,58]

# in 
if x in numbers:
   print(x in numbers)

# not in 
  
if x not in numbers:
   print(x not in numbers)

#Identity operators are used to check whether two variables refer to the same object in memory, not just whether their values are equal.

# is

if x is y:
   print(x is y)

# is not

if x is not y:
   print(x is not y)
   