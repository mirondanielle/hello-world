"""
Program: project2_surfaceArea.py
Author: Danielle Miron
Last date modified: 05/12/21

The purpose of this program is to calculate the surface area of a cube.  The first
input is an integer representing the edgeLength. The calculation of the surface area
is labeled as area. The output is an integer labeled as the surface area of a cube.

"""

#Requesting the input
edgeLength = int(input("Enter the length of the edge: "))

#Calculate the surface area
area = 6 * edgeLength ** 2

#Display the surface area
print("The cube's surface area is: " + str(area))

