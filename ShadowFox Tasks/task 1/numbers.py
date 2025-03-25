# task  2. Numbers
# 1. Function using format()
def formatted_string(num, char):
    return "The number is {} and the character is '{}'".format(num, char)

result = formatted_string(145, 'o')
print(result)
#2. Calculating Pond Area and Water Volume
# Given values
pi = 3.14
radius = 84
pond_area = pi * (radius ** 2) 
water_per_sq_meter = 1.4  
total_water = pond_area * water_per_sq_meter
print("Total Water in the Pond:", int(total_water))

# 3. Calculating Speed
# Given values
distance = 490 
time_in_minutes = 7  
time_in_seconds = time_in_minutes * 60 
speed = distance / time_in_seconds
print("Speed:", int(speed), "m/s")

