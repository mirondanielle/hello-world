import math
tolerance=0.00001
estimate=1.0
#Required function
def newton(num,estimate):

   #calculate the sqr root
   estimate=(estimate+num/estimate)/2
   difference =abs(num-estimate**2)
   if difference<= tolerance:
       return estimate
   else:
       #Return the result
       return newton(num,estimate)
def main():
  

   #infinite loop
   while True:
       try:
           x = float(input("Enter a positive number or enter/return to quit: "))
           print("The program's estimate: ",newton(x, estimate))
           print("Python's estimate: ",math.sqrt(x))
       except Exception as e:
           print(e)
           break
if __name__ == '__main__':
   main()

