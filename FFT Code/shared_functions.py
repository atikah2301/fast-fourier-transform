from shared_imports import *
# Functions which are used across multiple files


def rect_form(theta, r=1, is_rounded=True, decimal_places=15):
    """theta: float, r: float, is_rounded: bool, decimal_places: int
    Convert a complex number in exponential form to its rectangular form, a+bi
    Auxiliary to the FFT and IFFT function."""
    if is_rounded == True:
        return round(r * cos(theta), decimal_places), round(r * sin(theta), decimal_places)
    else:
        r * cos(theta), r * sin(theta)


def is_not_power_of_2(N):
    """N: int
    Use bit-wise operator trick to check for powers of 2.
    Auxiliary to the FFT function."""
    return True if N <= 0 or N & (N - 1) != 0 else False


def padding(P):
    """P: array of complex numbers
    Add 0s to the front of an array of coefficients to reach an array length that is a power of 2.
    Auxiliary to the FFT function."""
    N = len(P)
    next_pow_2 = pow(2, ceil(log(N) / log(2)))
    padding = next_pow_2 - N
    padded_polynomial = ([0] * padding) + P
    return padded_polynomial