from array import array

# Create an array of integers
my_array = array('i', [1, 2, 3, 4, 5])

# Print the original array
print("Original Array:", my_array)

# Insert an element (e.g., 10) at a specific location (index 2)
my_array.insert(2, 10)

# Print the modified array
print("Modified Array:", my_array)
