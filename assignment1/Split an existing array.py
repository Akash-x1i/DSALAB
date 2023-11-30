from array import array

# Create an array of integers
my_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the original array
print("Original Array:", my_array)

# Specify the lengths of the two new arrays
length1 = 3
length2 = 7

# Split the original array into two arrays
array1 = my_array[:length1]
array2 = my_array[length1:length1+length2]

# Print the two new arrays
print("Array 1:", array1)
print("Array 2:", array2)
