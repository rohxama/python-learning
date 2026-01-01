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