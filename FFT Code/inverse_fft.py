from shared_imports import *
from shared_functions import rect_form


def IFFT_recursion(P):
    """P: array of complex values
    Get coefficients from values of a polynomial.
    This algorithms has O(nlogn) time complexity."""

    N = len(P)

    # Check if the number of terms in the polynomial is a power of 2
    if N > 0 and N & (N - 1) != 0:
        return
        # need to pad the polynomial up

    # Base case: recursion stops when the polynomial is split into individual terms
    if N == 1:
        return P

    # Define the first of the Nth roots of unity
    a, b = rect_form(2 * pi / N)
    w = complex(a, -b)

    # Partition the polynomial by the parity of each term's position
    P_even, P_odd = P[0::2], P[1::2]

    # Recursive call to keep splitting the polynomial in half
    V_even, V_odd = IFFT_recursion(P_even), IFFT_recursion(P_odd)

    # Create a empty array to store the polynomial's values in
    coeff_rep = [0] * N

    # Calculate values in half the expected time by exploiting symmetries
    for k in range(N // 2):
        coeff_rep[k] = V_even[k] + W[k] * V_odd[k]
        coeff_rep[k + N // 2] = V_even[k] - W[k] * V_odd[k]

    return coeff_rep

def IFFT(P):
    """
    Final steps after IFFT_recursion.
    """
    # Create a copy of the argument data
    A_val = [val for val in P]
    A_coeff = IFFT_recursion(A_val)
    # Divide each resulting coefficient value by N
    A_coeff = [c / len(A_coeff) for c in A_coeff]

    return A_coeff[::-1]

if __name__ == '__main__':
    A_val = [(20+0j), (-5-5j), (-2+0j), (-5+5j)] # [2, 3, 7, 8]
    A_coeff = IFFT(A_val)
    print(A_coeff)
    print(A_val)