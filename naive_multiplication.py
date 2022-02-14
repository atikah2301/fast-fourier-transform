def naive_multiplication(A: list[int], B: list[int]):
    n_A = len(A)
    n_B = len(B)

    d_A = n_A - 1


d_B = n_B - 1

# Get the degree and number of terms for the new polynomial, C(x)
d_C = d_A + d_B
n_C = d_C + 1

# Initialise an array to store the coefficeints of C(x)
C = [0 for i in range(n_C)]

for i in range(n_A):
    for j in range(n_B):
        C[i + j] = C[i + j] + A[i] * B[j]

return C

A = [2, 3, 7]
B = [1, 0, 2]
naive_multiplication(A, B)