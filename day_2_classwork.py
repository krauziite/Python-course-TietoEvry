#Excercise no1
#Write a program that asks for and saves a username
#Ask a question about the user's age, using the username in the question.
#Shows in how many years the user will be 100 years old smile
#BONUS: Let the program also show the year when the user will be 100 years old.
#It could use a variable with the current year.
#It would be even better to get the current year automatically
#then you will need two additional lines:
#import datetime # let's talk about imports separately
#currentYear = datetime.datetime.now (). year

name = input("Enter your name, please: ")
username = input("Enter your username, please: ")
age = input(f"{username}, what is your age? ")

age=int(age)
age_hh = 100-age
age_h = input(f"You will be hundred in {age_hh} years")

currentYear = datetime.datetime.now().year
year = int(currentYear + age_hh)
print( f"{username} will turn 100 by {currentYear}")


#Excercise no2
#Ask user to input 3 numbers - width, length, height
width = input("Enter the width of the room in meters, please:\n")
length = input("Enter the length of the room in meters, please:\n")
height = input("Enter the height of the room in meters, please:\n")

#Find the volume of the room
#PS Think about units and what is the most appropriate data type for this
width = float(width) # no error handling here
length = float(length)
height = float(height)
volume = width * length * height
print(f"The volume of the room is {round(volume,2)} m\u00B3") # ³
print("\n")

#Excercise no3
# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: fahrenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision
precision = 4
# t = input("What is the temperature in Celsius?\n")
# t = float(t) # so we are using float because
t = float(input("What is the temperature in Celsius?\n")) # same as above two lines

t_fahrenheit = 32 + t * (9 / 5)
print("Current temperature in Celsius is", round(t, precision), sep=": ")
print(f"Current temperature in Celsius is: {round(t, precision)}")
# so three ways of formatting results here
print("Current temperature in Fahrenheit is", round(t_fahrenheit, precision), sep=": ")
print("Current temperature in Fahrenheit is: " + str(round(t_fahrenheit, precision))) #need to cast to str
print(f"Current temperature in Fahrenheit is: {round(t_fahrenheit, precision)}") # my favorite
# also there is a way to format inside strings without round
