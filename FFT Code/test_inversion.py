from fft import FFT
from inverse_fft import IFFT
from numpy import mean


def test_forward_inversion(coeffs):
    error = [abs(coeff_1 - coeff_2) for coeff_1, coeff_2 in zip(coeffs, IFFT(FFT(coeffs)))]
    print(f"Forward Inversion Error = {error}")
    if mean(error) < 0.001:
        print("Inversion Successful")
    else:
        print("Inversion Failed")

def test_backward_inversion(values):
    error = [abs(value_1 - value_2) for value_1, value_2 in zip(values, FFT(IFFT(values)))]
    print(f"Backward Inversion Error = {error}")
    if mean(error) < 0.001:
        print("Inversion Successful")
    else:
        print("Inversion Failed")

if __name__ == '__main__':
    coeffs = [(2 + 0j), (3 + 0j), (7 + 0j), (8 + 0j)]
    values = [(20 + 0j), (-5 - 5j), (-2 + 0j), (-5 + 5j)]
    test_forward_inversion(coeffs)
    test_backward_inversion(values)