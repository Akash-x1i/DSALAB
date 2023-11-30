from array import array

# Create an array of integers
my_array = array('i', [1, 2, 3, 4, 5])

# Print the original array
print("Original Array:", my_array)

# Remove the element at a specific location (index 2) using slicing
index_to_remove = 2
my_array = my_array[:index_to_remove] + my_array[index_to_remove + 1:]

# Print the modified array
print("Modified Array:", my_array)
