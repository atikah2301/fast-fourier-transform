from header import *

def rect_form(theta, r=1, is_rounded=True, decimal_places=15):
    if is_rounded == True:
        return round(r * cos(theta), decimal_places), round(r * sin(theta), decimal_places)
    else:
        r * cos(theta), r * sin(theta)


def FFT(P):
    """
    Return the DFT of a list of complex numbers, P.
    This algorithms has O(nlogn) time complexity.
    """

    N = len(P)

    # Check if the number of terms in the polynomial is a power of 2
    if N & (N-1) != 0:
        return
        # need to pad the polynomial up

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
    A_coeff = A = [2, 3, 7, 8] #[1,2,3,4]
    A_val = FFT(A_coeff)
    print(A_val)