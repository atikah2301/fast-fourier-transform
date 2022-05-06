from header import *
from rounding import *


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


def FFT_recursion(P):
    N = len(P)

    # Base case: recursion stops when the polynomial is split into individual terms
    if N == 1:
        return P

    # Define the first of the Nth roots of unity
    a, b = rect_form(2 * pi / N) # Takes the angle as argument
    w = complex(a, b)

    # Partition the polynomial by the parity of each term's position
    P_even, P_odd = P[0::2], P[1::2]

    # Recursive call to keep splitting the polynomial in half
    V_even, V_odd = FFT_recursion(P_even), FFT_recursion(P_odd)

    # Create a empty array to store the polynomial's values in
    value_rep = [0] * N

    # Calculate values in half the expected time by exploiting symmetries
    for n in range(N // 2):
        # print(value_rep)
        # print(n)
        value_rep[n] = V_even[n] + (w ** n) * V_odd[n]
        value_rep[n + N // 2] = V_even[n] - (w ** n) * V_odd[n]

    return value_rep


def is_not_power_of_2(N):
    return True if N <= 0 or N & (N - 1) != 0 else False


def FFT(P):
    """
    Prepare the argument to pass to the FFT_recursion function.
    """
    # Create a deep copy of the argument to not alter it
    A_coeff = [coeff for coeff in P][::-1]
    N = len(A_coeff)
    # Use a bitwise AND operation to test if the array length is a power of 2
    if is_not_power_of_2(N):
        A_coeff = padding(A_coeff)
    A_val = FFT_recursion(A_coeff)

    return A_val


if __name__ == '__main__':
    A_coeff = [6, 4, 2, 3, 7j] # Gets padded and becomes [0, 2, 3, 7j]
    A_val = FFT(A_coeff)
    print(round_nums(A_val))
