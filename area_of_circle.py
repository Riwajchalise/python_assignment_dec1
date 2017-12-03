from math import *
#functon to calculate area of a circle
def radius_circle(radius):
    a = pi*radius**2
    print("the area of the circle with radius {0} is {1:.3f}".format(radius,a) )

#main program
radius = input("enter the radius of circle: ")
radius = int(radius)
radius_circle(radius)


