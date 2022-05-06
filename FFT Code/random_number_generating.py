import numpy as np
from numpy.random import random_sample as np_rand
from fft import FFT
from inverse_fft import IFFT


def random_polynomial(n=1, min=-1000, max=1000, is_complex=False):
    diff = max - min
    if is_complex == True:
        return [complex(min + np_rand() * diff, min + np_rand() * diff) for _ in range(n)]
    else:
        return [min + np_rand() * diff for _ in range(n)]


if __name__ == "__main__":
    rand_pol = random_polynomial(n=3)
    fft_rand_pol = FFT(rand_pol)
    ifft_rand_pol = IFFT(fft_rand_pol)
    print(rand_pol)
    print(fft_rand_pol)
    print(ifft_rand_pol)
