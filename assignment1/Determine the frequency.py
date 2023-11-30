from array import array

# Create an array of integers
my_array = array('i', [1, 2, 3, 4, 2, 5, 2, 6, 7, 2])

# Print the original array
print("Original Array:", my_array)

# Specify the element to find the frequency of (e.g., 2)
element_to_count = 2

# Count the frequency of the specified element manually
frequency = sum(1 for item in my_array if item == element_to_count)

# Print the result
print(f"The frequency of {element_to_count} in the array is:", frequency)
