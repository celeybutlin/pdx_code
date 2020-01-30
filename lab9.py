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

VERSION 4: Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

(the table below only renders correctly with Markdown Navigator)

| - |ft|mi|m|km| |-|-|-|-| |ft|1||0.3048|| |mi||1|1609.34| |m|1/0.3048|1/1609.34|1|1/1000| |km|||1000|1|

But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi


"""
# # VERSION 1
# feet = float(input('How many feet? '))
# meters = feet * 0.3048
# print(meters)


# # VERSION 2
# distance = float(input('What is the distance? '))
# units = input('What are the units? ft, mi, m, or km? ')

# if units == "mi":
#     meters = distance * 1609.34
# elif units == "ft":
#     meters = distance *0.3048
# elif units == "m":
#     meters = distance
# elif units == "km":
#     meters = distance * 1000

# print(f'{distance} {units} is {meters} meters')


# # VERSION 3
# conversion = {
#     "in" : 0.0254,
#     "ft" : 0.3048,
#     "yd" : 0.9144,
#     "m" : 1,
#     "mi" : 1609.34,
#     "km" : 1000
# }

# distance = float(input('What is the distance? '))
# units = input('What are the units? in, ft, mi, yd, m, or km? ')

# distance_meters = distance * conversion[units]

# print(f'{distance} is {distance_meters} meters')


# VERSION 4
conversion = {
    "in" : 0.0254,
    "ft" : 0.3048,
    "yd" : 0.9144,
    "m" : 1,
    "mi" : 1609.34,
    "km" : 1000
}

distance = float(input('What is the distance? '))
unit_input = input('What are the units? in, ft, mi, yd, m, or km? ')
unit_output = input('What unit do you want to convert it to? in, ft, mi, yd, m, or km? ')

if unit_input not in conversion or unit_output not in conversion:
    print("Please enter a valid unit.")
    quit()

distance_meters = distance * conversion[unit_input]
distance_choice = distance_meters / conversion[unit_output]


print(f'{distance} {unit_input} is {distance_choice} {unit_output}')



