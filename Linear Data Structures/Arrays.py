# Create an initial list
Food = ["Coconuts", "Cherry"]

# Add data to the array
Food.append("Apple")
Food.append("Banana")
Food.append("Orange")
Food.append("Cherry")
Food.append("Jackfruit")

# Array length
print("Length of Food:", len(Food))

# Insert data at index 0
Food.insert(0, "Mango")  # Adding 'Mango' at the beginning of the list

# Extend the list with another list
Food.extend(["Alex", "John"])

# Print the list
print("Food List:", Food)

# Remove a specific item (check if it exists first)
if "Orange" in Food:
    Food.remove("Orange")

# Print the list after removing
print("Updated Food List:", Food)

# Remove and get the last element using pop()
last_item = Food.pop()
print("Last Item Removed:", last_item)

# Find the index of 'Coconuts'
try:
    position = Food.index("Coconuts")
    print("Index of 'Coconuts':", position)
except ValueError:
    print("'Coconuts' is not found!")

# Check and find the index of 'Cherry'
if "Cherry" in Food:
    position = Food.index("Cherry")
    print("Index of 'Cherry':", position)
else:
    print("'Cherry' not found in the list")

# Count occurrences of 'Banana'
if "Banana" in Food:
    count = Food.count("Banana")
    print("Count of 'Banana':", count)

# Reverse the list
Food.reverse()  # In-place reverse
print("Reversed Food List:", Food)

# Sort the list
Food.sort()  # In-place sort (alphabetical order)
print("Sorted Food List:", Food)

# Alternatively, use sorted() for a new sorted list
sorted_food = sorted(Food)
print("New Sorted Food List:", sorted_food)
