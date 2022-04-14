from math import cos, sin, pi


def rect_form(theta, r=1, is_rounded=True, decimal_places=15):
    if is_rounded == True:
        return round(r * cos(theta), decimal_places), round(r * sin(theta), decimal_places)
    else:
        r * cos(theta), r * sin(theta)


def DFT_real_input(X):
    """
    For an array of real numbers, return its DFT as an array of complex numbers.
    Complex numbers are given as arrays of length 2,
    where the first element is the real component and second element is the imaginary component.
    This algorithm has O(N^2) time complexity.
    """
    N = len(X)
    Y = [[0, 0] for _ in range(N)]

    for k in range(N):  # k=0,1,2
        for n in range(N):  # n=0,1,2
            theta = -2 * pi * n * k / N
            a, b = rect_form(theta)
            a, b = round(a * X[n], 8), round(b * X[n], 8)
            # print(f"{a} + {b}i")
            Y[k] = [round(Y[k][0] + a, 5), round(Y[k][1] + b, 5)]

        print(Y[k])


def complex_mult(w, v):
    """
    For two iterables in the forms [a, b] and [c, d] where a, b, c, d are real numbers,
    return [ac - bd, bc + ad], which represents their product as a complex number.
    """
    return [w[0]*v[0] - w[1]*v[1], w[1]*v[0] + w[0]*v[1]]


def DFT_complex_input(X):
    """
    For an array of complex numbers, return its DFT as an array of complex numbers.
    Complex numbers are given as arrays of length 2,
    where the first element is the real component and second element is the imaginary component.
    This algorithm has O(N^2) time complexity.
    """
    N = len(X)
    Y = [[0, 0] for _ in range(N)]

    for k in range(N):  # k=0,1,2
        for n in range(N):  # n=0,1,2
            theta = -2 * pi * n * k / N
            a, b = rect_form(theta)
            a, b = complex_mult([a,b], X[n])
            a, b = round(a, 8), round(b, 8)
            print(f"{a} + {b}i")
            Y[k] = [round(Y[k][0] + a, 5), round(Y[k][1] + b, 5)]

        print(Y[k])

if __name__ == '__main__':
    A = [2, 3, 7, 8]
    B = [1, 0, 2]

    # Polynomials A and B evaluated at the 1st, 2nd, and 3rd roots of unity
    DFT_real_input(A)

    #C = [[2,1],[3,2],[0,5]]
    C = [[2,1],[3,1],[7,1]]
    # DFT_complex_input(C)



