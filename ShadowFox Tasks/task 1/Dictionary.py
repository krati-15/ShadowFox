
#List of Friends and Name Lengths
# Step 1: List of friends' names
friends = ["abhi", "parth", "Sam", "Ravi", "ajay"]

# Step 2: Create a list of tuples (name, name_length)
name_lengths = [(friend, len(friend)) for friend in friends]

# Step 3: Print results
print("List of names with their lengths:")
for name, length in name_lengths:
    print(f"{name}: {length} characters")




# Travel Expense Tracker
# Step 1: Define expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Step 2: Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Step 3: Print total expenses
print(f"Your total expenses: ${your_total}")
print(f"Your partner's total expenses: ${partner_total}")

# Step 4: Determine who spent more
if your_total > partner_total:
    print("You spent more overall.")
elif your_total < partner_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

# Step 5: Identify significant expense differences
print("\nExpense Differences:")
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff >= 100:  # Consider $100 as a significant difference
        print(f"{category}: Difference of ${diff}")
