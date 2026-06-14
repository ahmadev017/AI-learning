# python has function for creating, reading, and deleting files
 

#Open a file
myFile = open('myFile.txt','w')

# Get some info
print('name', myFile.name)
print('is Closed : ', myFile.closed)
print('Opening Mode', myFile.mode)

#write to file 
myFile.write('Ilove pakistan')
myFile.write(' and javascript')
myFile.close()

# Append to file
myFile = open('myFile.txt','a')
myFile.write(' I also like php')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)

print(text)
