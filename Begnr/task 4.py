# Task 4: If Conditions

# 1. BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

# 2. Country from city
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print("City not found in database.")

# 3. Compare 2 cities
city1 = input("\nEnter first city: ")
city2 = input("Enter second city: ")

def country_of(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return "Unknown"

country1 = country_of(city1)
country2 = country_of(city2)

if country1 == country2 and country1 != "Unknown":
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
