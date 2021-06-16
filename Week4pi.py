iterations = int(input("Enter the number of iterations: "))
piFour = 0
numerator = 1
denominator = 1

for count in range(iterations):
    piFour += numerator / denominator
    numerator = -numerator
    denominator += 2

print("The aprroximation of pi is", piFour * 4)
