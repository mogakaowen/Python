# Program to display the Fibonacci sequence up to n-th term
nterms=int(input("How many terms in the Fibonacci series do you want to print? "))
#First two terms
n1=0
n2=1
print('The terms are: ')

for i in range(0, nterms):
   print(n1, end=" ")
   nth=n1+n2
   n1=n2
   n2=nth
   i+=1

#Program to check if a number is an Armstrong number
num = int(input("Enter the number to determine if it is an Armstrong number: "))

# Changed num variable to string, and calculated the length (number of digits)
order = len(str(num))
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# Program to check Armstrong numbers in a certain interval
lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))
print(f'The Armstrong numbers between {lower} and {upper} are: ')

for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0

   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** order
      temp //= 10

   if num == sum:
      print(num, end=" ")

# Display the powers of 2 using anonymous function
terms = int(input('How many terms? '))
# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

# Python program to convert decimal into other number systems
dec = int(input("Enter the decimal value to be converted: "))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

# Program to find the ASCII value of the given character
import string
for letter in string.ascii_lowercase:
    print("The ASCII value of '" + letter + "' is", ord(letter))

#Print the alphabet
print("Alphabet from a-z:")
for letter in string.ascii_lowercase:
   print(letter, end =" ")
print("\nAlphabet from A-Z:")
for letter in string.ascii_uppercase:
   print(letter, end =" ")

# Python program to shuffle a deck of card
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

# Program to display calendar of the given month and year
import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))