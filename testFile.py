nepal = "meroDesh"
print(nepal)

a,d,r = 5, 7, "hello again"
b = 9
c = d + b
print (c,d,r)

#data types and print in different format
print("{} {} {}".format("Oh hi",r,a))

#what kind of data type
print (type(r))

values = [1,2,"Selenium", 9.9, 67]

print(values[-1])
print (type(values))
print(values[1])
print(values[2:5])

values.insert(2, "testme")
print(values)

values.append("ohwow")
print(values)

values[3] = "mygod"
print(values)

del values[-1]
print(values)

print("test")