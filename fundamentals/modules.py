#A module is simply a Python file containing reusable code (functions, variables, classes)

import datetime
from datetime import date
import time
from time import time
from camelcase import CamelCase


#today = datetime.date.today()


# import custom module
import fundamentals.validator as validator
from fundamentals.validator import validate_email

email = 'test#test.com'
if validate_email(email):
 print('Email is valid')
else:
 print('Email is not valid') 

today = date.today()
timestamp = time()

print(today)

c= CamelCase()
print(c.hump('hello there world'))

print(timestamp)