from shared_imports import *
from naive_polynomial_multiplication import naive_multiplication
from fft_polynomial_multiplication import FFT_multiplication

def test_timing(f):
    """For an algorithm defined as a function, f,
    time its completion on different input sizes.
    Tabulate and return the time taken"""

    k = list(range(5, 15)) # range of input sizes to use input sizes
    n = [2**i for i in k] # all input sizes in an array
    number_of_tests = len(n)
    timings = [] # store the timings

    for i in range(number_of_tests):
        # Generate two polynomials of random coefficients
        A = [randint(0, 999) for _ in range(n[i])]
        B = [randint(0, 999) for _ in range(n[i])]

        t = time() # start timer
        f(A, B) # run algorithm
        t = time() - t # stop timer
        timings.append(t) # save the time
        print(f"{i+1}/{number_of_tests} tests done! n={n[i]} run complete! Time taken: {t}")

    # Tabulate and print
    table = {"n": n, "time (s)": timings}
    print(f"{f.__name__.replace('_', ' ')}:")
    print(tabulate(table, headers="keys"))

    return timings, n, k

if __name__ == '__main__':
    test_timing(naive_multiplication)
    test_timing(FFT_multiplication())

