import math
r,h = float(input("enter radius of cylinder ")), float(input("enter height of cylinder "))
a = 2*math.pi*r*r + 2*math.pi*r*h
print("surface area of this cylinder is ",a)