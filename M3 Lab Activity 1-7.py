#Cole Nelson.
#10/16/2021


#prints hello world
print("hello world")


#at asks the user for their name and prints it
name = input("Enter your name: ")
print("Hello", name + "!")


#asks for your name and says hi
username = input("Login: (Full Name) - ")
user1 = "Dr. Antonio Tovar"
user2 = "Cole Nelson"
if username == user1:
    print("Hello Dr. Antonio Tovar")
elif username == user2:
    print("Hello Cole Nelson")


#asks for a certain name and says hi otherwise says Access denied
username = input("Login: (Full Name) - ")
user1 = "Dr. Antonio Tovar"
user2 = "Cole Nelson"
if username == user1:
    print("Hello Dr. Antonio Tovar")
elif username == user2:
    print("Hello Cole Nelson")
else:
    print("Access denied")


#computes the area of a circle
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#Computes MPG for a car
miles_driven = float(input('\nEnter number of miles driven: '))
gallons_of_gas_used = float(input('Enter gallons of gas used: '))
mpg = miles_driven / gallons_of_gas_used
print('This is the MPG =', mpg, end='\n\n')


#Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))


#vaca time
vacationStart=int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for monday, etc.) '))
vacationLength=int(input('How many days will your vacation be? '))
returnDay=(vacationLength+vacationStart)%7
print(returnDay)