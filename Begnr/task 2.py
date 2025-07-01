# Task 2: Numbers

# 1. Format function with 145 and 'o'
formatted_string = format(145, 'o')  # Octal representation
print("Formatted (Octal) of 145:", formatted_string)

# 2. Area of a circular pond
radius = 84
area = 3.14 * radius ** 2
print("Area of pond:", int(area))

# Water calculation
water_per_sqm = 1.4
total_water = int(area * water_per_sqm)
print("Total water in liters (no decimal):", total_water)

# 3. Speed in m/s
distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60
speed = int(distance / time_seconds)
print("Speed (m/s):", speed)
