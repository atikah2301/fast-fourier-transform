

def multiply_values(A, B):
    """The function two arrays of length n containing complex numbers, and carries out an element-wise multiplication.
    The function returns the product as an array of length n."""
    C = [0 for _ in range(len(A))]
    for i in range(len(C)):
        C[i] = A[i]*B[i]
    return C

if __name__ == '__main__':
    A = [(1+0j), 1j, (-1+0j), (-0-1j)]
    B = [(1+0j), 1j, (-1+0j), (-0-1j)]
    C = multiply_values(A, B)
    print(C)