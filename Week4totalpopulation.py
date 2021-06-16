numberOfOrganisms = int(input("Enter the number of inital organisms: "))
growthRate = int(input("Enter the rate of growth: "))
numberOfHours = int(input("Enter the number of hours it takes to achieve the rate: "))
populationNumberOfHours = int(input("Enter the number of hours for which the population grows: "))


if(numberOfOrganisms >= 1):
    totalPopulation = int((populationNumberOfHours / numberOfHours) * growthRate
                           * numberOfOrganisms)
    print("The prediction of the total population is:",totalPopulation)

else:
    print("This is not a valid input")
    


