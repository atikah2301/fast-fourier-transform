from header import *
from multiply_values import multiply_values

def FFT_multiplication(A_coeff, B_coeff):
    # Step 1 - Evaluting
    A_val = scipy_fft(A_coeff)
    B_val = scipy_fft(B_coeff)
    # Step 2 - Multiplying
    C_val = multiply_values(A_val, B_val)
    # Step 3 - Interpolation
    C_coeff = scipy_ifft(C_val)

    return C_coeff



if __name__ == '__main__':
    A = np.array([2, 3, 7])
    B = np.array([1, 0, 2])
    # expected output from naive multiplication: [2, 3, 11, 6, 14]
    # C = FFT_multiplication(A, B)
    # print(C)

    D = [2, 3, 7, 8]
    values_D = scipy_fft(D)
    print(values_D)

    E = values_D
    coeff_E = scipy_ifft(E)
    print(coeff_E)