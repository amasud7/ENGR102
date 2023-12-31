# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Javier Aguilar
#               David Xue
#               Ayad Masud
#               Usamah Alghamdi
# Section:      511
# Assignment:   12.13 LAB: Matplotlib Example
# Date:         10 November 2023
# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material
#Comment
import numpy as np
import matplotlib.pyplot as plt

# part 1
x=np.linspace(-2, 2)
y1 = (1/4*2) * (x**2)
y2 = (1/4*6) * (x**2)
plt.plot(x, y1, 'b', linewidth=2.0)
plt.plot(x, y2, 'r', linewidth=6.0)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Parabola plots with varying focal length")
plt.legend(["f=2","f=6"])
plt.show()

# part 2
x = np.linspace(-4, 4, 25)
y = 2*(x**3) + 3*(x**2) - 11*x - 6
plt.scatter(x, y, color='y', marker='*')
plt.title('Plot of Cubic Polynomial')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

# Part 3
x = np.linspace(-2*np.pi, 2*np.pi)
y = np.cos(x)
y1 = np.sin(x)

plt.subplot(2,1,1)
plt.plot(x, y, 'r', label='cos(x)') 
plt.title('Plot of cos(x) and sin(x)')
plt.ylabel('y=cos(x)')
plt.legend()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(x, y1, 'b', label='sin(x)')
plt.ylabel('y=sin(x)')
plt.xlabel('x')
plt.legend()
plt.grid(True)
plt.show()

