# Example 1
grades = [87, 93, 75, 100, 82, 91, 85]   # this creates a list
grades[1] = 10  # these following lines add values to specific places in the list
grades[2] -= 90
grades[3] = grades[1]+grades[2]     # this accesses values within the list and adds them. 
print(grades[3])   # this prints out negative 5

# Example 2
grades = [87, 93, 75, 100, 82, 91, 85]
sum = 0
for i in range(7):   # looping through all values in list
    sum += grades[i]   # each iteration will increase the sum.
average = sum/7    # finally find the average of the grades.
print(average)

# Example 3
grades = [87, 93, 75, 100, 82, 91, 85]
sum = 0
for i in range(len(grades)):   # same as previous examples just using length of the list instead.
    sum += grades[i]
average = sum/len(grades)
print(average)

# Example 4
grades = [87, 93, 75, 100, 82, 91, 85]
sum = 0
for i in grades:   # same as previous example except it uses the actual loop at the iterative item. 
    sum += i
average = sum/len(grades)
print(average)

# Example 5
grades = [87, 93, 75, 100, 82, 91, 85]
for i in grades:
    i = 0   # this does not change the value in the list, just assigns the variable i with a value each time

# Example 6
grades = [87, 93, 75, 100, 82, 91, 85]
for i in range(len(grades)):
    grades[i] = 0    # this is how you access the actual element and change it within a loop

# Example 7
for i in range(10):    # range is basically is a list
    print(i)
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:  # this is equal to using range(10)
    print(i)

# Example 8
grades = [87, 93, 75, 100, 82, 91, 85]  # creates list
grades.append(80)   # adds 80 to the end of the lsit
print(grades)
print(len(grades))

# Example 9
list1 = [1, 2, 3]  
list2 = [4, 5, 6]
list3 = list1+list2   # adds the two lists together.
print(list3)    # this outputs [1, 2, 3, 4 , 5, 6]

# Example 10
grades = [87, 93, 75, 100, 82, 91, 85]
grades += [80]   # we can add lists instead of using .append()
j = 95
grades += [j]  # you have to make sure to make the object a list otherwise it doesnt work
print(grades)
print(len(grades))

# Example 11
grades = [87, 93, 75, 100, 82, 91, 85]
print(grades[0], grades[6])   # this prints 87 85

# Example 12
grades = [87, 93, 75, 100, 82, 91, 85]
print(grades[7])   # this results in out of bounds error

# Example 13
grades = [87, 93, 75, 100, 82, 91, 85]
print(grades[-1])   # using negatives will go from the back of the list, so this would print 85

# Example 14
grades = [87, 93, 75, 100, 82, 91, 85]
print(grades[-7])   # this prints 87
print(grades[-8])   # this results in out of bounds error

# Example 15
grades = [87, 93, 75, 100, 82, 91, 85]
print(grades[0:3])   # this prints [87, 93, 75]
print(grades[4:5])   # this prints [82]
print(grades[-3:-1])  # this prints [82, 91]

# Example 16
grades = [87, 93, 75, 100, 82, 91, 85]
print(grades[:3])   # this prints [87, 93, 75]
print(grades[4:])   # this prints [82, 91, 85]
print(grades[:])    # this prints the entire list

# Example 17
grades = [87, 93, 75, 100, 82, 91, 85]  # slicing does not result in out of bounds error, just goes to end or beginning. 
print(grades[4:300])
print(grades[-100:-3])

# Example 18
grades = [87, 93, 75, 100, 82, 91, 85]
sublist = grades[1:4]
print(grades)   # this prints [87, 93, 75, 100, 82, 91, 85]
print(sublist)  # this prints [93, 75, 100]

# Example 19
grades = [87, 93, 75, 100, 82, 91, 85]
sublist = grades[1:4]
sublist = []
print(grades)   # this prints [87, 93, 75, 100, 82, 91, 85]
print(sublist)  # this prints []

# Example 20
grades = [87, 93, 75, 100, 82, 91, 85]
sublist = grades[1:4]
grades[1:4] = []
print(grades)   # this prints [87, 82, 91, 85]
print(sublist)   # this prints [93, 75, 100]

# Example 21
grades = [87, 93, 75, 100, 82, 91, 85]
sublist = grades[1:4]
grades[5:5] = [65, 50]
print(grades)   # prints [87, 93, 75, 100, 82, 65, 50, 91, 85]
print(sublist)   # prints [93, 75, 100]

# Example 22
name = "Texas A&M University"
print(name[6:9])  # prints A&M
name[6:9] = []   # this results in error because strings cannot to item assignment.

# Example 23
city_name = "Dallas"
city_name[:4]
city_name[-4:]

# Example 24
city_name = "arp"
city_name[:4]
city_name[-4:]  # even though there is less than 4 characters it prints everything out because we don't get range errors with slicing

# Example 25
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid[0][0])   # this prints out 1
print(grid[1][2])   # this prints out 6

# Example 26
age = {'John' : 21, 'Jill' : 21}  # creates a dictionary
age['James'] = 20    # sets key James with value 20
age['Jessica'] = 23
print(age)
for i in age :
    print("key", i, ", value",age[i])
if 'James' in age:
    print("Yes for James")
else:
    print("No for James")
if 'Joe' in age:
    print("Yes for Joe")
else:
    print("No for Joe")