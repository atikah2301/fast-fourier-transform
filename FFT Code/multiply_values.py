def multiply_values(A, B):
    """A and B are arrays of complex numbers.
    Carries out an element-wise multiplication, returns the product as an array"""
    C = [0 for _ in range(len(A))]
    for i in range(len(C)):
        C[i] = A[i]*B[i]
    return C

if __name__ == '__main__':
    A = [(1+0j), 1j, (-1+0j), (-0-1j)]
    B = [(1+0j), 1j, (-1+0j), (-0-1j)]
    # A = [1, 0, 1]
    # B = [3, 4] # to check padding..
    C = multiply_values(A, B)
    print(C)