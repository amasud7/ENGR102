# Example 1
print('''He said "I'm tired." ''')
 # or
print("""He said "I'm tired.'""")

print('He said "I\'m tired." ')
# or
print("He said \"I'm tired.\"")

# Example 2
x = 2 # Integer
x = 2.0 # Floating point
x = "True" # String (x=True would be boolean)
x = 2 + 3 # Integer
x = 2.0 + 3.0 # Floating point
x = 2 / 3 # Floting point
x = 2 / 2 # Floating point (Dividing integers yields floating point)
x = 2 // 2 # Integer (this is integer division - no remainder)

# Example 3
x = 1 + 2
print(x) # output = 3

# Example 4
x = 1.0 + 2.0
print(x) # output = 3.0

# Example 5
x = "1" + "2"
print(x) # output = 12

# Example 6
print(3*"Howdy") # output = HowdyHowdyHowdy

# Example 7
float(3) # this becomes 3.0
x = 2 # integer value of 2
y = float(x) # y has value 2.0 

# Example 8
int(2.0) # has value 2
int(3.14) # has value of 3
int(4.9) # has value of 4
int(0.01) # has the value of 0
int(-1.3) # has the value -1
int(-1234.56) # has the value of -1234

# Example 9
int('3') # has the integer value of 3
float('3.14') # this has the floating point value of 3.14
float('2') # has the floating point value of 2.0
int('2.5') # error, does NOT convert to float then to int 

# Example 10
str(1) # has the string value of '1'
str(2.5) # has the string value of '2.5'
str(1/2) # has the string value of '0.5'
str(10 * 1.0) # has the string value of '10.0'

# Example 11
int(True) # has the value of 1
float(True) # has the value of 1.0
float(False) # has the value of 0.0
bool(0) # has the boolean value of False
bool(3) # has the boolean value of True
bool('0.0') # has the boolean True because its a string
bool('0') # has the boolean True because its a string.
bool('False') # has the value True because its a string. 

# Example 12
test = str(float(str(3/2)+str(int(3/2))))*int(int(str(2)+str(7))/int(10.3))

# Example 13
print(type(test)) # this is type string.

# Example 14
x=3 
y=4
print(x,':',y) # 3 : 4 ---> has spaces
print(str(x) + ':' + str(y)) # 3:4 ---> no spaces

# Example 15 (can change the space around characters)
"2.3".ljust(10) # has value: '2.3 '
"2.3".rjust(10) # has value: ' 2.3'
"2.3".center(10) # has value: ' 2.3 '

# Example 16
print("example 16")
print("Test",3,5)
print("Test",3,5,sep=',')
print("Test",3,5,sep=',',end=':')
print(15)

# Example 17
from math import *
r = float(input())
print(pi*r**2)

# Example 18 (asking user for input)
from math import *
print("Enter the radius of a circle:")
r = float(input())
print("The area of the circle is "+str(pi*r**2))

# Example 19
from math import *
r = float(input("Enter the radius of a circle: "))
print("The area of the circle is " + str(pi*r**2))

# Example 20
from math import *

# function definition.
def area_of_circle(radius):
    area = pi * radius ** 2
    print("The area of the circle is {:.4f}".format(area))

# function call
r = float(input("Enter the radius of circle 1: "))
area_of_circle(r)
r = float(input("Enter the radius of circle 2: "))
area_of_circle(r)