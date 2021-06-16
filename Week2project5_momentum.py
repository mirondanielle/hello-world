"""
Program: project5_momentum.py
Author: Danielle Miron
Last date modified: 05/12/21

The purpose of this program is to calculate the momentum. The first
input is a float labeled mass and it is the object's mass.The second
input is a float labeled velocity and it is the object's velocity.
The calculation is labeled as momentum which is mass * velocity.
The output is the momentum of the object. 

"""
#Request the inputs
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

#Calculate the momentum
momentum = mass * velocity

#Display the momentum
print("The momentum of the object is: " + str(momentum) + " kg*m/s")
