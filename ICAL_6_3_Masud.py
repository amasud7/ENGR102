# Exercise 1
a = 0
while a == 0:
    print("About to change a")
    a = 1
    print("Changing a back to 0")
    a = 0
# this loop will result in an infinite loop

# Exercise 2
i = 0
while i <= 10:  # better to write i <= 10 than i < 11 bc it says how many times the loop actually run.
    print("Doing something")
    i += 1
# this is a very common loop, something that runs for a given number of times and does something each time. 
# this is usually better to be done with a for loop

# Exercise 3
for i in range(10):  # the range is 0 to 9 NOT 0 to 10 (it stops one before the number given as parameter)
    print("Doing Something")

# Exercise 4
# for loop
for i in range(10):
    print("Doing Something")

# while loop
i = 0
while i < 10:
    print("Doing something")
    i += 1
# both of these loops do the same thing, the for loop for this case is better because you know how many times the loop has to run.

# Exercise 5
sum = 0  # this program sums all the number within the range given. 
for i in range(10): # since the range is 0 to 9 you have to add one extra each time (better to just make the range 1 to 11 if you want to add numbers 1 to 10)
    sum += i + 1
print(sum)
# the formula for summing numbers is n(n+1)/2

# Exercise 6
for i in range(3):
    print("i is", i)
    for j in range(3):
        print(" j is", j)
        break
# the inner loop reaches break before it can ever get to the next number in the range so it exits that loop. but keeps looping in the loop oustide of it. 

# Exercise 7
for i in range(10):
    if i % 2 == 1:
        continue
print("i is", i)
# for odd numbers (where the remainder was anything but 0), continue ends the iteration before it prints, however it prints the even numbers.

# Exercise 8
x_o = input("Enter a number: ")
x = float(x_o)
while x > 1:
    x /= 2
    if x == 1:
        print(f"{x_o} is a power of 2")
        break
else:
    print(f"{x_o} is not a power of 2")

# the else statement only runs if the loop before it ends naturally (without break) 