# details enter

name = input("enter drivers name")
license_plate = input("enter your license_plate number")
check_in = int(input("when the car enter in 'use 24 hour formate like 14 for 2 PM' "))
check_out = int(input("when you goes out 'use 24 hours formate' "))
duration = float(check_out-check_in)

# details of car and driver
print("car driver name ",name.capitalize())
print("car license plate number ",license_plate.upper())

# rate of parking
print("rate of parking is 5$ per hour")

print("total duration of car park in parking lot")
total_cost = duration * 5
print(total_cost,"$")

