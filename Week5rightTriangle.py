side1 = int(input("Enter the length of side one: "))
side2 = int(input("Enter the length of side two: "))
side3 = int(input("Enter the length of side three: "))

if ((side1* side2 + side2*side2 == side3*side3) or (side2*side2 + side3*side3 == side1*side1) or
    (side3*side3 + side1*side1 == side2*side2)):

        print("The triangle is a right triangle.")

else:
        print("The triangle is not a right triangle.")

