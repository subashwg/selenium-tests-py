file = open('test.txt')

#read the n numbers of the characters
# print(file.read(3))

#read contents of the first line
# print(file.readline())

#print line by line using readline method
# line = file.readline()
# while line != "":
#     print (line)
#     line = file.readline()

#print line by line using readlines method
for line in file.readlines():
    print(line)

file.close()