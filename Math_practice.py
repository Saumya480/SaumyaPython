# #Write a Python program to convert degree to radian.
from math import pi
degree = float(input("Enter angle in degrees: "))
radian=degree * (pi / 180)
print(f"{degree} degrees is equal to {radian:} radians")
#
# #Write a Python program to convert radian to degree.
# from math import pi
#
# radian=float(input("Enter angle in radian :"))
# degree=radian * (180 /pi)
# print(f"{radian} radian is equal to {degree:} degrees")

#Write a Python program to calculate the area of a parallelogram.

# base=float(input("Enter base value of the parallelogram :"))
# height=float(input("Enter height value of the parallelogram :"))
# Area=base*height
# print(f"The area of the parallelogram is {Area:} square units")
#Write a Python program to calculate surface volume and area of a cylinder.
# from math import pi
# height=float(input("Enter the height value of the cylinder :"))
# radius=float(input("Enter the radius value of the cylinder:"))
# volume=pi *radius**2*height
# surface_area=2*pi*radius*(radius+height)
# print(f"Volume of the cylinder: {volume:} cubic units")
# print(f"Surface area of the cylinder: {surface_area:} square units")

#Find the area of a Circle
# import math
# radius=float(input("Enter the radius of a circle :"))
# area=math.pi*radius**2
# print(f"The area of a circle is {area} square units :")
 # Find the smallest value from the given List of numbers
# x = [ 45, -5, 0, 5, 45 ]
# print("The smallest  value of given list of  number is :",min(x))
# Find the highest value from the given List of numbers
# x = [ 45, -5, 0, 5, 45 ]
#
# print("The highest  value of given list of  number is :",max(x))

# Accept two numbers from the user and calculate multiplication
# num1=float(input("Enter the first number :"))
# num2=float(input("Enter the second number :"))
# result=num1*num2
# print(f"The multiplication  of {num1} and {num2}is {result}")
# Display “My Name Is James” by entering your name instead of the hardcoded name "James"
# uname=str(input("Enter user Name :"))
# print("User Name is :" + uname)
# Accept length and width measurement of a square from the user and display the area square
# lengh= float(input("Enter the length of the square :"))
# area=lengh**2
# print(f"The area of the square  is {area} square units")

# Accept radius measurement of a circle from the user and display the area of the circle
# from math import *
# radius=float(input("Enter the radius of the circle :"))
# area=pi*radius**2
# print(f"The area of the circle is {area} square units")

# Accept radius measurement of a sphere from the user and display the volume of the sphere
from math import *
radius=float(input("Enter the radius of the sphere :"))
volume=(4/3)*pi*radius**3
print(f"The volume of a sphere is {volume} square units")


