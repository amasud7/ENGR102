# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:     Ayad Masud
# Section:    511
# Assignment: 7.28 LAB: Kaprekar's Constant
# Date:       6 October 2023 
#Take input
digit=int(input("Enter a four-digit integer: "))

number=int(digit)

iterations=0
while number!=6174 and number !=0:
    if number>=1000:
        number=f'{number:0>4}'
        n1="".join(sorted(number))
        n2="".join(reversed(n1))
        n=int(n2)-int(n1)
        print(number,"> ",end=' ')
        number=n
        iterations=iterations+1
    else:
        print(number,"> ",end=' ')
        number=f'{number:0>4}'
        n1="".join(sorted(number))
        n2="".join(reversed(n1))
        n=int(n2)-int(n1)
        number=n
        iterations=iterations+1
if number==6174:
    print(number)
else:
    print(0)
    iterations=iterations
print(digit,f"reaches {number} via Kaprekar's routine in",iterations,"iterations")



