#JS uses function
#Python uses def
#JS uses { }
#Python uses indentation

#create function

def sayHello(name = 'hamad'):
  print(f'Hello {name}')
sayHello('Ahmad')

#return value 
def getValue(a,b):
  result=a+b
  return result
num=getValue(5,4)
print(num)



#A lambda function in Python is a small anonymous (unnamed) function that can have only one expression
# Python lambda ≈ JavaScript arrow function with an implicit return and only a single expression

getSum = lambda num1,num2:num1+num2

print(getSum(10,5))