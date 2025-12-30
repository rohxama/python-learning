## First ever python code jo har koi likhta hai mn nay bhi likh lye ✅
print("hello World")

## Making a variable or bhayia itna asaan kayyy mazaa aagaya ✅
rohama = 23
print(rohama) 

## Datatypes wo bhi sirf 5 (int, str, bool, float, complex) jo main hain ✅
a = 1 # interger wrote as int
b = "Rohama" # string wrote as str
c = 0.5 # float 
d = 3/2 # complex
e = True # Boolean wrote as bool 
f = False # Boolean wrote as bool 
g = 'Salfi' # string 

## Checking the type of varaible ✅
print(type(a)) 

## Type casting ✅
age = "28"
print(age, type(age))

age = int(age)
print(age, type(age))  # Same as str(value), bool(value), float(bool) and so on....

# Ab agr boolean ke bt kee jaaye kay issko kse krna hai toh iss mein aa jati hain 2 values truthy and falsy, ab yahn asay maan lo kay sb data types, sb values truthy hoti hain means true, and kuch hee values falsy hoti hain jase kay (0, none, "", undefined, False, {}, []). Ab agr variables mein falsy values ayyein toh samaj lena ye false hain or baqi sb values true.

## Use of Input (we have to take some input from user) ✅

yourAge = input("Enter your age ?")
print(yourAge)

## Escape Sequences (/n, /t, /b etc) ✅

print("My name is Rohama\nMy Age is 20.")

## Raw Strings (use to stop the functionality of escape sequence) ✅

print(r"For new line we use \n")

## Formated Strings (to use the variable values in result) ✅

myName = "Rohama"
print(f"My name is {myName}")

## Arithmetic Operators ✅

print(2 + 3) # Add both numbers
print(3 - 4) # Subtract both numbers
print(5 * 8) # Multiply both numbers
print(2 / 9) # Divide both numbers but gives you values in float
print(2 // 5) # Divide both numbers but gives you value in integer
print(3 ** 0) # Its means 3 ke power zero
print(3 % 5) # Gives remainder of both numbers

## Comparison Operators is used b/w 2 numbers (answer will always in boolean) ✅

print(5 > 6) # greater than
print(4 < 3) # less than
print(3 == 4) # equal to
print(2 != 4) # not equal to
print(2 <= 4) # equal and less than
print(4 >= 3) # equal and greater than

## Logical Operator (and, or, not) ✅

print(2 > 3 and 4 < 5) # Only true when both conditions are correct
print(3 < 7 or 6 > 2) # Only true when only one or both condition are correct
print(not 4 > 2) # it reverse the answer

## If/else statement ✅

myAge = int(input("My age is: "))
if myAge >= 18:
    print("You can vote")
else:
    print("Sorry, you can't vote")