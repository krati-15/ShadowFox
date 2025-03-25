# Step 1: Define the initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Step 2: Calculate and print the number of members
print(f"Number of members: {len(justice_league)}")

# Step 3: Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Updated list after adding Batgirl & Nightwing:", justice_league)

# Step 4: Move Wonder Woman to the beginning (making her the leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Updated list after making Wonder Woman the leader:", justice_league)

# Step 5: Separate Aquaman and Flash by moving Green Lantern between them
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("Updated list after separating Aquaman & Flash:", justice_league)

# Step 6: Replace the entire Justice League with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

# Step 7: Sort the list alphabetically (new leader will be the first in the list)
justice_league.sort()
print("Sorted Justice League:", justice_league)
print(f"New leader: {justice_league[0]}")
