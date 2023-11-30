def add_polynomials(poly1, poly2):
    """
    Adds two polynomials represented by their coefficient lists.
    
    Args:
    - poly1: Coefficients of the first polynomial (e.g., [3, 0, -1] represents 3x^2 - 1)
    - poly2: Coefficients of the second polynomial
    
    Returns:
    - Coefficients of the sum of the two polynomials
    """
    len1, len2 = len(poly1), len(poly2)
    max_len = max(len1, len2)

    # Pad the shorter polynomial with zeros
    poly1 += [0] * (max_len - len1)
    poly2 += [0] * (max_len - len2)

    # Perform element-wise addition
    result = [coef1 + coef2 for coef1, coef2 in zip(poly1, poly2)]

    return result

# Example usage:
poly1 = [3, 0, -1]  # represents 3x^2 - 1
poly2 = [1, -2, 4]  # represents x^2 - 2x + 4

result = add_polynomials(poly1, poly2)
print("Sum of the polynomials:", result)
