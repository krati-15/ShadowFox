#task 4 if condition 
#1. BMI Category Program
# Step 1: Ask the user for their height and weight
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))

# Step 2: Calculate BMI using the formula
bmi = weight / (height ** 2)

# Step 3: Determine the BMI category based on the result
if bmi >= 30:
    category = "Obesity"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Underweight"

# Step 4: Display the result in a friendly way
print(f"Your BMI is {bmi:.2f}, which means you are in the '{category}' category.")

 #2. City to Country Lookup

# Step 1: Define cities and their countries
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Step 2: Ask the user for a city name
city = input("Enter a city name: ").strip()

# Step 3: Check which country the city belongs to
found = False
for country, cities in countries.items():
    if city in cities:
        print(f"{city} is in {country}.")
        found = True
        break

# Step 4: Handle the case where the city isn't found
if not found:
    print("Sorry, I don't recognize that city.")

# 3.check if two cities belong to the same country.

# Step 1: Define cities and their countries
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Step 2: Ask the user for two city names
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Step 3: Find which country each city belongs to
country1 = country2 = None

for country, cities in countries.items():
    if city1 in cities:
        country1 = country
    if city2 in cities:
        country2 = country

# Step 4: Check if both cities were found and compare them
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}.")
    else:
        print("They don't belong to the same country.")
elif not country1 and not country2:
    print("Sorry, neither of the cities are recognized.")
elif not country1:
    print(f"Sorry, {city1} is not in the list.")
else:
    print(f"Sorry, {city2} is not in the list.")
