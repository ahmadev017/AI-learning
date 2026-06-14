

import json

# sample json

userJSon = '{"first_name":"Ahmad","last_name":"Raza","age":22}'

#parse to dict

user = json.loads(userJSon)

print(user)
print(user['first_name'])

#dict to json
car={'make':'Ford','model':'Mustang','year':1970}

carJson = json.dumps(car)

print(carJson)