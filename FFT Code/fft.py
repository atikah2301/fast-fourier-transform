from shared_imports import *
from rounding import *
from shared_functions import is_not_power_of_2, padding, rect_form

def FFT_recursion(P):
    """P: array of complex values
    Get values from coefficients of a polynomial.
    This algorithms has O(nlogn) time complexity."""

    N = len(P)

    # Base case: recursion stops when the polynomial is split into individual terms
    if N == 1:
        return P

    # Define the first of the Nth roots of unity
    a, b = rect_form(2 * pi / N) # Takes the angle as argument
    w = complex(a, b)
    W = [w**k for k in range(N // 2)]  # Store the first n/2 n-th roots of untiy

    # Partition the polynomial by the parity of each term's position
    P_even, P_odd = P[0::2], P[1::2]

    # Recursive call to keep splitting the polynomial in half
    V_even, V_odd = FFT_recursion(P_even), FFT_recursion(P_odd)

    # Create a empty array to store the polynomial's values in
    value_rep = [0] * N

    # Calculate values in half the expected time by exploiting symmetries
    for k in range(N // 2):
        # print(f"n = {k}, w^n = {W[k]}")
        value_rep[k] = V_even[k] + W[k] * V_odd[k]
        value_rep[k + N // 2] = V_even[k] - W[k] * V_odd[k]

    return value_rep


def FFT(P):
    """
    Prepare the argument to pass to the FFT_recursion function.
    """
    # Create a copy of the argument to not alter it
    A_coeff = [coeff for coeff in P][::-1]
    N = len(A_coeff)
    # Use a bitwise AND operation to test if the array length is a power of 2
    if is_not_power_of_2(N):
        A_coeff = padding(A_coeff)
    A_val = FFT_recursion(A_coeff)

    return A_val


if __name__ == '__main__':
    A_coeff = [2, 3, 7, 8]
    A_val = FFT(A_coeff)
    print(A_coeff)
    print(A_val)  # should return [(20+0j), (-5-5j), (-2+0j), (-5+5j)]
