# Many companies wish to understand the needs and wants of their customers more deeply so the company can create products that fill those needs and wants.
# One way to understand customers more deeply is to record the values entered by customers while they are using a program and then to analyze those values.
# One common way to record values is for a program to store them in a file.

import math
from datetime import datetime

current_date_and_time = datetime.now()

w = int(input("Please Enter the first number(width): "))
a = int(input("Please Enter the second number(aspect ratio): "))
d = int(input("Please Enter the third number(diameter): "))
v = (math.pi * w * w * a * (w * a + 2540 * d))/ 10000000000
v = round(v,2)


# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volumes_file:
   
    print(current_date_and_time, file=volumes_file)
    print(f" Width of the tire: {w}, aspect ratio of the tire:  {a}, diameter of the wheel:  {d}, volume of the tire: {v}", file=volumes_file)
###########################################
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

age = int(input("Please Enter your age: "))
maximumRate = 220 - age
heartRate65 = int(maximumRate * 65/100)
heartRate85 = int(maximumRate * 85/100)
print(f"When you exercise to strengthen your heart, you should keep your heart rate between: {heartRate65} and {heartRate85} heart rate per minute.")

#############################################
# A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
#Write a Python program named boxes.py that asks the user for two integers:  1) the number of manufactured items and 
#2) the number of items that the user will pack per box. Your program must compute and print the number of boxes necessary to hold the items. 
#This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
import math
numItems = int(input("Enter the number of items: "))
numItemsperBox = int(input("Enter the number of items per box: "))
result = numItems / numItemsperBox
result = math.ceil(result)
print(f"For {numItems} items, packing {numItemsperBox} items in each box, you will need {result} boxes")
#########################################

from datetime import datetime

current_date_and_time = datetime.now()

#day_of_week = current_date_and_time.weekday()

day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


day_of_week = 1
print(day[day_of_week])

subtotal = 0


price = ''

while price != 'done':
    price = input("enter the price: ")
    if price != 'done':
        subtotal += float(price)
    
if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    print(f"Subtotal: ${subtotal}")

    discount = 0.10 
    amount_discount = subtotal * discount
    total = subtotal - amount_discount
    print(f"Discount: ${amount_discount:.2f}")
    tax = 0.06
    amount_tax= total * tax
    new_total = total + amount_tax
    print(f"taxes: ${amount_tax:.2f}")
    print(f"your new total + tax: ${new_total:.2f}")
elif (day_of_week== 1 or day_of_week == 2) and subtotal < 50:
    difference = 50 - subtotal
    print(f"To get a discount it is lefting ${difference}")
else:
    tax = 0.06
    amount_tax= subtotal * tax
    new_total = subtotal + amount_tax
    print(f"taxes: ${amount_tax:.2f}")
    print(f"Total: ${new_total:.2f}")

    ########################################

    """ Write a Python program named fuel_usage.py that asks the user for three numbers:

1. A starting odometer value in miles
2. An ending odometer value in miles
3. An amount of fuel in gallons
Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers. 
Your program must have three functions named as follows:

1. main
2. miles_per_gallon
3. lp100k_from_mpg
All user input and printing must be in the main function. 
In other words, the miles_per_gallon and lp100k_from_mpg functions must not call the the input or print functions. 
To start your program, copy and paste the following code into your program and use it as a design as you write your program."""

def main():
    # Get an odometer value in U.S. miles from the user.
    start_odometer = int(input("Enter the value of initial odometer: "))

    # Get another odometer value in U.S. miles from the user.
    end_odometer = int(input("Enter the value of final odometer: "))
    
    # Get a fuel amount in U.S. gallons from the user.
    fuel = float(input("Enter fuel amount value: "))
    
    # Call the miles_per_gallon function and store the result in a variable named mpg.
    mpg = miles_per_gallon(start_odometer, end_odometer, fuel)
    
    # Call the lp100k_from_mpg function to convert the miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    
    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 1)
    
    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)
    
    # Display the results for the user to see.
    print(f"The result of fuel efficiency miles per gallon is: {mpg} and liters per 100 kilometers: {lp100k} ")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
     mpg = (end_miles - start_miles) / amount_gallons
     return mpg


def lp100k_from_mpg(mpg):
     lp100 = 235.215/mpg
     return lp100


# Call the main function so that
# this program will start executing.
main()

##################################
#You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days.
# On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.

from datetime import datetime
weekday = ("Monday(0)","Tuesday(1)", "Wednesday(2)","Thursday(3)","Friday(4)", "Saturday(5)", "Sunday(6)")

current_date_and_time = datetime.today().weekday()
amount = int(input("Enter the price: "))
if(amount >= 50 and current_date_and_time == 1 or current_date_and_time == 2):
    amount = amount - amount*0.10
    print(f"You have a discount of 10% today. You total is: ${amount}")
else:
    amount = amount + amount*0.06
    print(f"Your total is: ${amount}")

###############################
