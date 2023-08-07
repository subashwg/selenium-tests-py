#if/else condition

greeting = "Buenos dias"
maths = 45

if maths<56:
    print ("Si")
    print ("hola")
else:
    print ("no, lo siento")


#for loop condition

numbers = [1,2,3,4,6,8,9]
for i in numbers:
    print(i*2)
print("*******************************")

#syntax with first and last index
#sum of first five natural numbers
#range (i,j) -> i to j-1

summation = 10
for j in range(1,7):
    #print(j)
    summation = summation + j
    print(summation)
print("*******************************")

#syntax with range and specific iteration count to jump
#programming examples(print numbers from 1 to 10 with summation)

for k in range(1, 20, 4):
    print(k)
print ("********************")


#syntax with only upper bound
#printing numbers serially
for m in range(20):
    print(m)