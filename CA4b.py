
#----------------------------------------------------------------------------------------------
#        1- ADDITION
#----------------------------------------------------------------------------------------------
	
# def add (first,second) :
	#return first + second
	
# Getting input number from users	
first = int(raw_input("enter first number to add "))	
second = int(raw_input("enter second number to add "))

# using lambda function to add 2 numbers and printing that
addition = lambda x,y: x + y
print "The answer is ", (addition(first,second))
print
# Using map lambda to calculate vectors
print ("Now let's try the map function as well ")

print 
print "The vectors are: \n a = [1,2,3,4] \n b = [17,12,11,10] \n c = [-1, -4, 5, 9] "

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]
print
print "a + b + C is equal to ", map(lambda x,y,z: x + y, a,b,c)
print "and"
print "a + b - C is equal to ", map(lambda x,y,z: x + y - z, a,b,c)
print "and"
print "a - b - C is equal to ", map(lambda x,y,z: x - y - z, a,b,c)

print
print "Let's try Reduce function for the list below \n 47,11,42,13 "

v = reduce(lambda x,y: x-y, [47,11,42,13])
print "The answer for the reduce function is ",v
print
#----------------------------------------------------------------------------------------------
#       2- Subtraction
#----------------------------------------------------------------------------------------------

# def subtract (first,second):
	# return first - second
first = int(raw_input("enter first number, the order is: first number minus second number "))	
second = int(raw_input("enter the second number you want to be subtracted from first number "))
subtract = lambda x,y: x - y
print (subtract(first,second))

#----------------------------------------------------------------------------------------------
#       3- MULTIPLICATION
#----------------------------------------------------------------------------------------------	
# def multiply (first,second):
#	return first * second
	
first = int(raw_input("enter the first number to multiply "))	
second = int(raw_input("enter the second number to multiply "))

multiply = lambda x, y: x * y 
print (multiply(first,second))

#----------------------------------------------------------------------------------------------
#        4- DIVISION
#----------------------------------------------------------------------------------------------
	
# def divide (first,second):
	# if second == 0:
		# return 'inf'
	# else:
		# return first / second
		
first = int(raw_input("enter the number you want to divide by "))
second = int(raw_input("enter the number you want to be divided by "))

divide = lambda x,y: x / y 

print (divide(first,second))

#----------------------------------------------------------------------------------------------
#         5- EXPONENT
#----------------------------------------------------------------------------------------------	
	
# def exponent (first,second):		
	# return first ** second

x = int(raw_input("enter the base number "))	
y = int(raw_input("enter the power "))

exponent = lambda x, y: x ** y 
print (exponent(x,y))

#----------------------------------------------------------------------------------------------
#         6- SQUARE
#----------------------------------------------------------------------------------------------	
	
# def square (first,second):
	# if first == 0:
		# return 0
	# elif second == 2:
		# return first ** second	
x = int(raw_input("enter the base number you want to square  "))
y = 2	

square = lambda x, y: x ** y 
print (square(x,y))

print
print ("Let's try a list comprehension ")

# using the list comprehension for the range of 10
x = (x **2 for x in range(10))
print(x)

x = list(x)
print(x)

#----------------------------------------------------------------------------------------------
#         7- CUBE
#----------------------------------------------------------------------------------------------	
	
# def cube (first,second):
	# if first == 0:
		# return 0
	# elif second == 3:
		# return first ** second	
x = int(raw_input("enter the base number you want to raise to the power of three "))
y = 3	

cube = lambda x, y: x ** y 
print (cube(x,y))
print
# using the list comprehension for the range of 10
print ("Let's try a list comprehension ")
x = (x **3 for x in range(10))
print(x)

x = list(x)
print(x)		
		
#----------------------------------------------------------------------------------------------
#       8- SQUARE ROOT
#----------------------------------------------------------------------------------------------

# def squareRoot (n):
	# if n > 0:
		# return n ** 0.5	
	# if n == 0:
		# return 0
	# if n < 0:	
		# return 'inf'
# n = int(raw_input("enter a number "))
# print  n**0.5		
		
# n = int(raw_input("enter a number "))

# squareRoot = lambda x: n ** 0.5 
# print (squareRoot(x))




#----------------------------------------------------------------------------------------------
#        9- COSINE
#----------------------------------------------------------------------------------------------

# def cosine(a):
 #  c=math.cos(4)
#	return c

n =int(raw_input(" enter the number you wish to calculate cosine for "))
print(lambda y: (lambda x, y: x(x, y))(lambda x, y: y*x(x, y-1) if y > 0 else 1,y))(n)	
		

#----------------------------------------------------------------------------------------------
#        10- MODULO
#----------------------------------------------------------------------------------------------

# def modulo (first,second):
#	return first % second 

#Using filter function with modulo operation, the result is boolean: TRUE or FALSE
# TRUE
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result
print 
result = filter(lambda x: x % 2 == 0, fib)	
print result


	