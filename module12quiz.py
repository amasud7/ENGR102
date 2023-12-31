import numpy as np
file = open('module12quizF23.txt', 'r')
list = []
for i in file:
    list.append(i.strip())

list1 = [eval(i) for i in list]
matrix = np.array([list1]).reshape((100, 100))
#print(matrix)

k1 = matrix[0:5, 85].sum()
k2 = sum(matrix[4, :])/100
k3 = sum(matrix[62, -5:])
k4 = min(matrix[0, :])
k5 = max(matrix[29, :])
key = str(k1) + str(int(k2)) + str(k3) + str(k4) + str(k5)
key1 = 'howdy'
print(key)
