from shared_imports import *
from naive_polynomial_multiplication import naive_multiplication
from fft_polynomial_multiplication import FFT_multiplication

def test_timing(f):
    n = [10, 100, 1000] # input size
    timings = []

    for i in range(len(n)):
        A = [randint(0, 999) for _ in range(n[i])]
        B = [randint(0, 999) for _ in range(n[i])]

        t = time()
        f(A, B)
        t = time() - t
        timings.append(t)

    table = {"n": n, "time (s)": timings}
    print(f"{f.__name__.replace('_', ' ')}:")
    print(tabulate(table, headers="keys"))


if __name__ == '__main__':
    test_timing(naive_multiplication)
    test_timing(FFT_multiplication())

