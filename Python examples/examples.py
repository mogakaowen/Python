# Python Program to calculate the square root
num = float(input('Enter a number: '))

num_sqrt = num ** 0.5  #x**y=x times x y times eg 2**2=2*2*2
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

# Find square root of real or complex numbers
# Importing the complex math module
import cmath
num = eval(input('Enter a complex number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))


# Python program to swap two variables
x = input('Enter value of x: ')
y = input('Enter value of y: ')

#create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#OR
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

# Program to check if a number is prime or not
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than or equal to 1, it is not prime
else:
    print(num,"is not a prime number")


#Program to print all the prime numbers in a given interval
num1 = int(input("Enter the start of the interval: "))
num2 = int(input("Enter the end of the interval: "))
print(f'The prime numbers between {num1} and {num2} are: ')

for num in range(num1, num2 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
        print(num, end=' ')

# Python program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

# Python program to find the factorial of a number provided by the user using recursion
def factorial(x): 
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)
