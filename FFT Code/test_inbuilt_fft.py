from multiply_values import multiply_values
import numpy as np
from scipy.fft import fft, ifft

def FFT_multiplication(A_coeff, B_coeff):
    # Step 1 - Evaluting
    A_val = fft(A_coeff)
    B_val = fft(B_coeff)
    # Step 2 - Multiplying
    C_val = multiply_values(A_val, B_val)
    # Step 3 - Interpolation
    C_coeff = ifft(C_val)

    return C_coeff


if __name__ == '__main__':
    A = np.array([2, 3, 7])
    B = np.array([1, 0, 2])
    # expected output from naive multiplication: [2, 3, 11, 6, 14]
    C = FFT_multiplication(A, B)
    print(C)