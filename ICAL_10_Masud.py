a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))
try:
    c = a / b
except ZeroDivisionError:
    print("You can't divide by 0!")
    b = int(input("Enter a different denominator: "))
    c = a / b # We could have an error again!
print(c)