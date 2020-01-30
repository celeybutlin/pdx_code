"""This lab will involve writing a program that allows the user to convert a number between units.

VERSION 1: Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

VERSION 2: Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m

Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m

VERSION 3: Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

"""
# Version 1
feet = float(input('How many feet? '))
meters = feet * 0.3048
print(meters)

# Version 2
distance = float(input('What is the distance? '))
units = input('What are the units? ft, mi, m, or km? ')

if units == "mi":
    meters = distance * 1609.34
elif units == "ft":
    meters = distance *0.3048
elif units == "m":
    meters = distance
elif units == "km":
    meters = distance * 1000

print(f'{distance} {units} is {meters} meters')

# Version 3
conversion = {
    "in" : 0.0254,
    "ft" : 0.3048,
    "yd" : 0.9144,
    "m" : 1,
    "mi" : 1609.34,
    "km" : 1000
}

distance = float(input('What is the distance? '))
units = input('What are the units? in, ft, mi, yd, m, or km? ')

distance_meters = distance * conversion[units]

print(f'{distance} is {distance_meters} meters')
