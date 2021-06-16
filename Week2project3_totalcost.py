"""
Program: project3_totalcost.py
Author: Danielle Miron
Last date modified: 05/12/21

The purpose of this program is to calculate the total number of videos. I initialized new
as equaling 3.00 and old as equaling 2.00 because those are set amounts. The first
input is an integer labeled by newAmount and it is the number of new videos.The second
input is an integer labeled as oldAmount and it is the number of old videos.
The calculation is labeled as totalAmount which is the new multiplied by newAmount plus old
multiplied by the oldAmount. The output is the total cost of both new videos and old videos.

"""
#Initialzing the constants 
new = 3.00
old = 2.00

#Requesting the inputs for new and old videos
newAmount = int(input("Enter the number of new videos: "))
oldAmount = int(input("Enter the number of old videos: "))

#Calculating the total amount
totalAmount = new * newAmount + old * oldAmount

#Displaying the total cost 
print("The total cost is $" + str(totalAmount))
