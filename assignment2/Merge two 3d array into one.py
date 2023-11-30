def merge_3d_arrays(arr1, arr2):
    """
    Merge two 3D arrays into one.
    
    Args:
    - arr1: First 3D array
    - arr2: Second 3D array
    
    Returns:
    - Merged 3D array
    """
    merged_array = []

    # Merge each 2D layer of the arrays
    for layer1, layer2 in zip(arr1, arr2):
        merged_layer = []

        # Merge each row of the layers
        for row1, row2 in zip(layer1, layer2):
            merged_row = row1 + row2
            merged_layer.append(merged_row)

        merged_array.append(merged_layer)

    return merged_array

# Example usage:
array1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
array2 = [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]

merged_result = merge_3d_arrays(array1, array2)

# Print the merged 3D array
for layer in merged_result:
    print(layer)
