# Example 1
outfile = open("MyOutput.txt", 'w')
outfile.write("Testing the write command.\n")
x = 987
outfile.write("Here's a number: "+str(x)+'\n')
outfile.write("And another number:")
outfile.write(str(21))
outfile.write("\n")
outfile.close()


# Example 2
s = "1,2,3,4"
elems = s.split(',')
print(elems)

# Example 3
date = "10/21/2018"
parts = date.split('/')
month = parts[0]
day = parts[1]
year = parts[2]
print("Day:",day,"Month:",month,"Year:",year)
