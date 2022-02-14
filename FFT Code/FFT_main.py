from math import log
from math import exp
from math import pi


def partition_by_parity(P: list[int]):
    even = []
    odd = []
    for i in range(len(P)):
        if i % 2 == 0:
            even.append(P[i])
        else:
            odd.append(P[i])
    return even, odd


def FFT(P: list[int]):
    """Convert a list of n numbers, P,
    that represents the coefficients of a polynomial,
    to a point-value representation, using the FFT.
    Return a list of n complex numbers."""

    n = len(P)

    # Base Case of Recursion
    if n == 1:
        return P

    #     if log(n, 2).is_integer() == False:
    #         return # padding..

    # First root of unity
    w = complex(0, exp(2 * pi / n))

    # Recusion on the paritionted polynomial
    even, odd = partition_by_parity(P)
    y_e, y_o = FFT(even), FFT(odd)

    # Setup for calculating values by iteration
    y = [0] * n
    half = int(n / 2)

    for j in range(half):
        y[j] = y_e[j] + (w ** j) * y_o[j]
        y[j + half] = y_e[j] - (w ** j) * y_o[j]

    return y


print(FFT([1, 2, 3, 4]))