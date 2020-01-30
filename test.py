conversions = {
    "onefoot": 0.3048,
    "onemile": 1609.34,
    "onemeter": 1,
    "onekilometer": 1000
}
value = input("What type of unit do you want to convert from, feet to meters, miles to kilometers, meters to feet or kilometers to miles ")
inputValue = int(input("now input the number you'd like to find the conversion for!"))
if "feet to meters" == value:
    print(f" {inputValue * conversions['onefoot']}")
elif "miles to kilometers" == value:
    print(f" {inputValue * conversions['onefoot']}")
elif "meters to feet" == value:
    print(f" {inputValue * conversions['onefoot']}")
elif "kilometers to miles" == value:
    print(f" {inputValue * conversions['onefoot']}")
else:
    print("please try again")