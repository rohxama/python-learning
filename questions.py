# Accept two numbers and print the greatest between them

num1 = int(input("Print number1: "))
num2 = int(input("Print number2: "))
if num1 > num2:
    print(f"The greatest number between them is: {num1}")
elif num2 > num1:
    print(f"The greatest number between them is: {num2}")
else:
    print("Both numbers are equal")

# Accept the gender of teh user as a character and print the respective message on the basis of gender

gender = input("What's your gender F/M: ")
if gender == 'F':
    print("Good Morning Mam!")
elif gender == 'M':
    print("Good Morning Sir!")
else:
    print("Please try again")

# Accept an integer and check whether it is an even number or odd

num = int(input("Enter your number: "))
if num % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")

# Accept the name and age from the user and check if the user is valid voter or not

yourName = input("Enter your name: ")
yourAge = int(input("Enter your age: "))
if yourAge >= 18:
    print("You can vote")
else:
    print("No, you can't vote")

# Accept a year and check if it is leap year or not

year = int(input("Enter the year: "))
if year % 100 != 0 and year % 4 == 0:
    print("This is leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("This is leap year")
else:
    print("This is not a leap year") 

# Accept a character from user and check if it is vowel or consonent

inp = input("Enter your character: ")
if inp in "aeiouAEIOU":
    print("This is vowel")
else:
    print("This is consonent")

# Print number up to n

n = int(input("Enter a number: "))
for i in range(1,n+1,1):
    print(i)

# Reverse the loop n to 1

x = int(input("Enter a number: "))
for i in range(x,0,-1):
    print(i)

# Take a number as a input and print its table

tableOf = int(input("Enter your number: "))
for i in range(1,11,1):
    print(f"{tableOf} * {i} = {tableOf*i}")

# Sum up n number

y = int(input("Enter a number: "))
sum = 0
for i in range(1,y+1,1):
    sum = sum + i
print(sum)

# Find factorial of n number

f = int(input("Enter a number: "))
mul = 1
for i in range(1,f+1,1):
    mul = mul * i
print(mul)

# Find the factor of number

fact = int(input('Enter a number: '))
for i in range(1, fact+1, 1):
    if fact%i == 0:
        print(i)

# Accept a number and check if it is perfect number or not (If its factors sum except itself the number is equal to that number)

z = int(input("Enter a number: "))
m = 0
for i in range(1, z, 1):
    if z%i == 0:
        m = m + i
if m == z:
    print("It is a perfect number")
else:
    print("Not perfect number")

# Check if the number is prime or not (If its factor are more than 2)

pri = int(input("Enter your number: "))
count = 0
for i in range(1, pri + 1, 1):
    if pri%i == 0:
        count = count + 1
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")

# Accept a number and separate it

numbr = int(input("Enter a number: "))

while(numbr > 0):
    print(numbr%10)
    numbr = numbr // 10    

# Check if number is pallindromic (If number and its reverse in equal) or not

p = int(input("Enter a number: "))
rev = 0
copy = p

while(p > 0):
    t = p % 10
    rev = rev * 10 + t
    p = p // 10
if copy == rev:
    print("Pallindromic Number")
else:
    print("Not a Pallindromic number")

