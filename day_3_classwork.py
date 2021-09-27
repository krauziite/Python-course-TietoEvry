#1. Health check

#Ask user for their temperature.
#If the user enters below 35, then output "not too cold"
#If 35 to 37 (inclusive), output "all right"
#If the temperature  over 37, then output  "possible fever"

temp = int(input("What is your temperature?"))
if temp < 35:
    print("not too cold")
elif temp >= 35 and temp <= 37:
        print("all right")
else:
        print("possible fever")

#2. Xmas Bonus

#The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of service over 2 years.
#Task. Ask the user for the amount of the monthly salary and the number of years worked.
#Calculate the bonus.
#Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
#Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0).

salary = int(input("What is your salary?"))
years = int(input("How many years have you worked?"))

if years < 2:
    print(f"{years} years of experience, {salary} Euro salary, no bonus")
elif years> 2:
    bonus = int((years - 2) * (0.15 * salary))
    print(f"{years} of experience, {salary} Euro salary, the bonus will be {bonus} Euro")


#3. Ordered output.

#Ask the user to enter 3 numbers, output them in ascending order.
#Note: for now, we solve this task only with if, elif, else actions.
#There is also a solution using sorting and list structure, which we have not yet seen.

x = int(input("first number: "))
y = int(input("second number: "))
z = int(input("third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)

x = int(input('first number'))
y = int(input('second number'))
z = int(input('thirdnumber'))

numbers = [x, y, z]
list.sort(numbers)
print(numbers)
