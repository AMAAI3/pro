
import numpy as np

def strassen_matrix_multiply(A, B):
    n = len(A)

    # Base case: If the matrices are 1x1, just multiply and return
    if n == 1:
        return np.array([[A[0][0] * B[0][0]]])

    # Split matrices into quarters
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Recursive steps
    P1 = strassen_matrix_multiply(A11, np.subtract(B12, B22))
    P2 = strassen_matrix_multiply(np.add(A11, A12), B22)
    P3 = strassen_matrix_multiply(np.add(A21, A22), B11)
    P4 = strassen_matrix_multiply(A22, np.subtract(B21, B11))
    P5 = strassen_matrix_multiply(np.add(A11, A22), np.add(B11, B22))
    P6 = strassen_matrix_multiply(np.subtract(A12, A22), np.add(B21, B22))
    P7 = strassen_matrix_multiply(np.subtract(A11, A21), np.add(B11, B12))

    # Calculate result submatrices
    C11 = np.subtract(np.add(np.add(P5, P4), P6), P2)
    C12 = np.add(P1, P2)
    C21 = np.add(P3, P4)
    C22 = np.subtract(np.subtract(np.add(P5, P1), P3), P7)

    # Combine result submatrices into the final result
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

# Example usage
n = 2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = strassen_matrix_multiply(A, B)
print(result)


