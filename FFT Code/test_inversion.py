from fft import FFT
from inverse_fft import IFFT


def test_forward_inversion(coeffs):
    return [abs(coeff_1 - coeff_2) for coeff_1, coeff_2 in zip(coeffs, IFFT(FFT(coeffs)))]

def test_backward_inversion(values):
    return [abs(value_1 - value_2) for value_1, value_2 in zip(values, FFT(IFFT(values)))]

if __name__ == '__main__':
    coeffs = [(2 + 0j), (3 + 0j), (7 + 0j), (8 + 0j)]
    values = [(20 + 0j), (-5 - 5j), (-2 + 0j), (-5 + 5j)]
    print(test_forward_inversion(coeffs))
    print(test_backward_inversion(values))