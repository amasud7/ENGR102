# Example 1
def warn():
    print("********** WARNING!!! **********")
    print("You are about to do something dangerous!")
warn()

# Example 2
def warn():
    print("********** WARNING!!! **********")
    print("You are about to do something dangerous!")
def doublewarn():
    warn()
    warn()
doublewarn()

# Example 3
def my_function():
    a = 3
    print(a)

a = 5
print(a)
my_function()
print(a)

# Example 4
def my_function(x):
    x += 1
    print(x)

a = 5
print(a)
my_function(a)
print(a)

# Example 5
def F(x):
    x += 3

a = 5
F(a)
print(a)

# Example 6
def F(a):
    a += 3

a = 5
F(a)
print(a)  

# Example 7
def F():
    a += 3

a = 5
F()
print(a)

# Example 8
def F(a):
    print(a)

a = 5
b = 10
F(b)

# Example 9
def F():
    global a
    a += 3

a = 5
F()
print(a)

# Example 10
def twenty_one():
    return 21

a = twenty_one()
print(a)

# Example 11
def is_three_more(a, b):
    if a == b + 3:
        return True
    else:
        return False
    
print(is_three_more(10, 7))
print(is_three_more(1, 5))

# Example 12
def F(a):
    a += 1
    return a
    a += 10
    return a

x = F(4)
print(x)    # after using return statement, nothing afterwards runs

# Example 13
def F(a="Bryan", b="Texas", c="USA"):
    print(a, b, c)

F("Toronto", "Ontario", "Canada")
F("Orlando", "Florida")
F("Houston")
F()

# Example 14
def F(a, b="Texas", c="USA"):
    print(a, b, c)

F()   # error because there is no value for 'a' which is needed

# Example 15
def F(a, b="Texas", c='a'):   # error because b has a default value, but c comes after and also must have a default value. 
    print(a, b, c)

# Example 16
def dosomething(a, b):
    a += b
    b = 7

x = 1
y = 2
dosomething(x, y)
print(x)
print(y)

# Example 17
def dosomething(a, b):
    a += b
    b = 7

x = 1.0
y = 2.0
dosomething(x, y)
print(x)
print(y)

# Example 18
def dosomething(a, b):
    a += b
    b = 7

x = "Texas"
y = "Aggies"
dosomething(x, y)
print(x)
print(y)

# Example 19
def dosomething(a, b):
    a += b
    b = 7

x = [1]
y = [2]
dosomething(x, y)
print(x)
print(y)

# Example 20     assigning the entire list a new value does not change the original list. 
def dosomething(a):
    a = [10, 11, 12]

x = [1, 2, 3]
dosomething(x)
print(x)

# Example 21    assigning value like this changes orignal list
def dosomething(a):
    a[0] = 10

x = [1, 2, 3]
dosomething(x)
print(x)    

# Example 22
mylist = [1, 2, 3]  # myList2 points at the same object as mylist
mylist2 = mylist
mylist[0] = 24
print(mylist, mylist2)

mylist = [1, 2, 3]   # mylist2 creates a copy of mylist so it does not change values of both lists
mylist2 = mylist[:]
mylist[0] = 24
print(mylist, mylist2)
