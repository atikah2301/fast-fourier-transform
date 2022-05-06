from fft import FFT
from inverse_fft import IFFT
from multiply_values import multiply_values

def FFT_multiplication(A_coeff, B_coeff):
    # Step 1 - Evaluting
    A_val = FFT(A_coeff)
    B_val = FFT(B_coeff)
    # Step 2 - Multiplying
    C_val = multiply_values(A_val, B_val)
    # # Step 3 - Interpolation
    C_coeff = IFFT(C_val)

    return C_coeff

if __name__ == '__main__':
    # A = [2, 3, 7]
    # B = [1, 0, 2] # expected output from naive multiplication: [2, 3, 11, 6, 14]
    A = [1, 0, 1]
    B = [0, 3, 4] # expected output from naive multiplication: [3, 4, 3, 4]
    C = FFT_multiplication(A, B)
    print(C)