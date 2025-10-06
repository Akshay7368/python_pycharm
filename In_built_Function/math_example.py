import math

#Print absolute values from numbers
print(math.fabs(-66.43))
print(math.fabs(-7))

# Round a number downward to its nearest integer
print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(-5.3))
print(math.floor(22.6))
print(math.floor(10.5))
print("------------")
# Round a number upward to its nearest integer
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))
print("------------")

#Return the value of the first parameter and the sign of the second parameter
print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))

print("------------")

#Return factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))

print("------------")

# Print the square root of different numbers
print (math.sqrt(64))
print (math.sqrt (12))
print (math.sqrt (68))
print (math.sqrt (100))
print("------------")

# Round square root downward to the nearest integer
print (math.isqrt(10))
print (math.isqrt (12))
print (math.isqrt (68))
print (math.isqrt (100))

print("------------")

#Return the value of 9 raised to the power of 3
print(math.pow(9, 3))
print("------------")


# Return the truncated integer parts of different numbers
print(math.trunc(2.77))
print(math.trunc(8.33))
print(math.trunc(-99.01))
print("------------")


# Print the sum of all items
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))
print("------------")


# Return the sine of different values
print (math.sin(0.00))
print (math.sin(-1.23))
print (math.sin(10))
print (math.sin(math.pi))
print (math.sin(math.pi/2))

print("------------")

#find the  the greatest common divisor of the two integers
print (math.gcd(3, 6))
print (math.gcd(6, 12))
print (math.gcd(12, 36))
print (math.gcd(-12, -36))
print (math.gcd(5, 12))
print (math.gcd(10, 0))
print (math.gcd(0, 34))
print (math.gcd(0, 0))
print("------------")


# Return the remainder of x/y
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))

print("------------")


sequence = (2, 4, 2)
#Return the product of the elements
print(math.prod(sequence))

print("------------")

#find the exponential of the specified value
print(math.exp(65))
print(math.exp(-6.89))
print("------------")


# Return the natural logarithm of different numbers
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))
