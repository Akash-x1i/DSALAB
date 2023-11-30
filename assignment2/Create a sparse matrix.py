class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def add_element(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Invalid matrix indices")
        if value != 0:
            self.data[(row, col)] = value

    def to_dense_matrix(self):
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        return dense_matrix

# Example usage:
sparse_matrix = SparseMatrix(3, 3)

# Adding non-zero elements
sparse_matrix.add_element(0, 1, 3)
sparse_matrix.add_element(1, 0, 1)
sparse_matrix.add_element(2, 2, 4)

# Converting to a dense matrix for display
dense_matrix = sparse_matrix.to_dense_matrix()

# Print the sparse matrix
print("Sparse Matrix:")
for row in dense_matrix:
    print(row)
