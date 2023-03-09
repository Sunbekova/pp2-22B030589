#Write a Python program to calculate the area of a trapezoid.

h = float(input("Height: " ))
a = float(input("Base, first value: " ))
b = float(input("Base, second value: " ))

area = 0.5*((a + b)*h)   #Calculate the area of the trapezoid

print("Expected Output: ", area)   #Print the result