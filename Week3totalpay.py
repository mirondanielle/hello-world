"""
Program: totalpay.py
Author: Danielle Miron
Compute employee's total weekly pay

1. The inputs are
    hourly wages
    regualr hours
    overtime hours
2. Computations:
    total weekly hours = hourly wages * regular hours + overtime hours * hourly
    wages * 1.5
3. The outputs are
    total weekly pay

"""

hourlyWages = float(input("Enter the hourly wage: $ "))

regularHours = float(input("Enter the regular hours: "))

overtimeHours = float(input("Enter the overtime hours: "))

totalWeeklyPay = hourlyWages * regularHours + overtimeHours * hourlyWages * 1.5

print("The employees total weekly pay is: $" + str(round(totalWeeklyPay,2)))
