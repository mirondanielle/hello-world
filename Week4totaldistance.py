
initalHeight = int(input("Enter the inital height from which the ball is dropped: "))
bounceIndex = float(input("Enter the bounciness index of the ball: "))
numberOfBounces = float(input("Enter the number of times the ball is allowed to continue bouncing: "))

distance = 0.0

while numberOfBounces > 0:
    distance = distance + initalHeight
    initalHeight = initalHeight * bounceIndex
    distance = distance + initalHeight
    numberOfBounces -= 1
    

print("Total distance traveled is:",distance,"feet.")
