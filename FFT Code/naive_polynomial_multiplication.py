def naive_multiplication(A: list[int], B: list[int]):
    # Lengths & degrees of A(x) and B(x)
    n_A = len(A)
    n_B = len(B)
    d_A = n_A - 1
    d_B = n_B - 1

    # Degree & length of C(x), the product
    d_C = d_A + d_B
    n_C = d_C + 1

    C = [0 for i in range(n_C)]

    # Calculate new coefficients as the sum of pair-wise products of old coefficients
    for i in range(n_A):
        for j in range(n_B):
            C[i + j] = C[i + j] + A[i] * B[j]

    return C

if __name__ == '__main__':
    A = [2, 3, 7]
    B = [1, 0, 2]
    # expected output, from manual calculation: [2, 3, 11, 6, 14]
    C = naive_multiplication(A, B)
    print(C)