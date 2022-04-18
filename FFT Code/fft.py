from header import *

def rect_form(theta, r=1, is_rounded=True, decimal_places=15):
    if is_rounded == True:
        return round(r * cos(theta), decimal_places), round(r * sin(theta), decimal_places)
    else:
        r * cos(theta), r * sin(theta)


def padding(P):
    """
    Add 0s to the front of an array of coefficients to reach an array length that is a power of 2.
    """
    N = len(P)
    next_pow_2 = pow(2, ceil(log(N) / log(2)))
    padding = next_pow_2 - N
    padded_polynomial = ([0] * padding) + P
    return padded_polynomial


def FFT(P):
    """
    Return the DFT of a list of complex numbers, P.
    This algorithms has O(nlogn) time complexity.
    """

    N = len(P)

    # Base case: recursion stops when the polynomial is split into individual terms
    if N == 1:
        return P

    # Define the first of the Nth roots of unity
    a, b = rect_form(2 * pi / N)
    w = complex(a, b)

    # Partition the polynomial by the parity of each term's position
    P_even, P_odd = P[0::2], P[1::2]

    # Recursive call to keep splitting the polynomial in half
    V_even, V_odd = FFT(P_even), FFT(P_odd)

    # Create a empty array to store the polynomial's values in
    value_rep = [0] * N

    # Calculate values in half the expected time by exploiting symmetries
    for n in range(N//2):
        value_rep[n] = V_even[n] + (w ** n) * V_odd[n]
        value_rep[n + N//2] = V_even[n] - (w ** n) * V_odd[n]

    return value_rep


if __name__ == '__main__':
    A_coeff = A = [2, 3, 7] #[1,2,3,4]
    # Check if the number of terms in the polynomial is a power of 2
    # Using a trick involving the bitwise AND binary operator
    N = len(A_coeff)
    if N > 0 and N & (N-1) != 0:
        A_coeff = padding(A_coeff)
    A_val = FFT(A_coeff)
    print(A_val)