from header import *
from naive_polynomial_multiplication import naive_multiplication

def test_timing(f):
    n = [10, 100, 1000]
    times = []

    for i in range(len(n)):
        A = [randint(0, 999) for _ in range(n[i])]
        B = [randint(0, 999) for _ in range(n[i])]

        t = time()
        f(A, B)
        t = time() - t
        times.append(t)

    table = {"n": n, "time (s)": times}
    print(f"{f.__name__.replace('_', ' ')}:")
    print(tabulate(table, headers="keys"))


if __name__ == '__main__':
    test_timing(naive_multiplication)

# from n=100 to n=1000, x10 more data resulted in x16 runtime
# from n=1000 to n=10,000, x10 more data resulted in x100 runtime