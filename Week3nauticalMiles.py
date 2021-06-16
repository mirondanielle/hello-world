""""
Program: nauticalMiles.py
Author: Danielle Miron

1. The inputs are
    kilometers
2. Computations
    degrees per minute = 90 *60
    distance = oneKilometer = degressPerMinute/10000
    nautical mile = oneKilometer * Kilometers
3. The ouputs are
    nautical miles 
    
"""

#Request the input
Kilometers = int(input("Enter the number of Kilometers: "))

#Computation for degrees per minute
degreesPerMinute = 90*60

#Computation for distance 
oneKilometer = degreesPerMinute/10000

#Computation for nautical mile 
nauticalMile = oneKilometer*Kilometers

#Display the number of nautical mile 
print (Kilometers, "Kilometers equals", nauticalMile, "Nautical Miles")

