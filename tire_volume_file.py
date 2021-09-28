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
