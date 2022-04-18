from header import *

def rect_form(theta, r=1, is_rounded=True, decimal_places=15):
    if is_rounded == True:
        return round(r * cos(theta), decimal_places), round(r * sin(theta), decimal_places)
    else:
        r * cos(theta), r * sin(theta)


def IFFT(P):
    """
    Return the inverse DFT of a list of complex numbers, P.
    This algorithms has O(nlogn) time complexity.
    """

    N = len(P)

    # Check if the number of terms in the polynomial is a power of 2
    if N > 0 and N & (N-1) != 0:
        return
        # need to pad the polynomial up

    # Base case: recursion stops when the polynomial is split into individual terms
    if N == 1:
        return P

    # Define the first of the Nth roots of unity
    a, b = rect_form(2 * pi / N)
    w = -complex(a, b)

    # Partition the polynomial by the parity of each term's position
    P_even, P_odd = P[0::2], P[1::2]

    # Recursive call to keep splitting the polynomial in half
    V_even, V_odd = IFFT(P_even), IFFT(P_odd)

    # Create a empty array to store the polynomial's values in
    coeff_rep = [0] * N

    # Calculate values in half the expected time by exploiting symmetries
    for n in range(N//2):
        coeff_rep[n] = V_even[n] + (w ** n) * V_odd[n]
        coeff_rep[n + N//2] = V_even[n] - (w ** n) * V_odd[n]

    return coeff_rep


if __name__ == '__main__':
    A_val = A = [(20+0j), (-5-5j), (-2+0j), (-5+5j)] # [2, 3, 7, 8]
    A_coeff = IFFT(A_val)
    A_coeff = [c / len(A_coeff) for c in A_coeff]
    print(A_coeff)