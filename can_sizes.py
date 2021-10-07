"""Write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. 
Then visually examine the output and answer this question, "Which can size has the highest storage efficiency?"""

import math

def main():
    i = 0
    while i<=11:
        name = input("Enter the can name: ")
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        volume = cylinder_volume(radius, height)
        surface = cylinder_surface_area(radius, height)
        storageCan = volume / surface
        printCan(name, storageCan)
        i += 1


   
def printCan(name,storageCan):
    print(f"{name} : {storageCan: .1f}")

def cylinder_volume(radius, height):
    volume = math.pi * pow(radius, 2) * height
    return volume

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi*radius*(radius + height)
    return surface_area

main()