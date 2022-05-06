from multiply_values import multiply_values
from naive_polynomial_multiplication import naive_multiplication
from rounding import round_nums

def naive_polynomial_evaluation(P, X):
    """
    Evaluate the polynomial, P, given as an array of its coefficients at each of the values in array X
    Return an array, Y, where Y[i] = P(X[i])
    """
    Y = [0] * len(X)
    for i in range(len(X)):
        # Evaluate the polynomial at each X[i]
        for j in range(len(P)):
            # Evaluate each term of the polynomial at X[i] and add them
            Y[i] += P[j] * pow(X[i], len(P)-1-j)
    return Y

def lagrange_polynomial(X, i):
    X_ = X[:i] + X[i+1:] # all of X except X[i]

    denominator = 1
    for j in range(len(X_)):
        denominator *= X[i] - X_[j] # (xi - x1), (xi - x2), etc excluding (xi - xi)

    numerator = [1, -X_[0]]
    for j in range(1, len(X_)):
        factor = [1, -X_[j]] # (x - x1), (x - x2), etc excluding (x - xi)
        numerator = naive_multiplication(numerator, factor)

    return [numerator[j] / denominator for j in range(len(numerator))]

def lagrangian_polynomial_interpolation(X, Y):
    """
    Given length n arrays of X and Y values, return the coefficients of a unique degree n-1 polynomial
    """
    n = len(X)
    L = [lagrange_polynomial(X, i) for i in range(n)]

    YL = [0] * n # YL will be a list of the Y[i] * L[i] polynomials
    for i in range(len(L)): # For each polynomial in L
        YL[i] = [L[i][j]*Y[i] for j in range(len(L[i]))]  # Multiply each term in L_i(x) by y_i

    P = [0] * len(YL[0])
    for i in range(len(YL[0])): # For each term in a polynomial
        for j in range(len(YL)): # For the current polynomial
            P[i] += YL[j][i]

    return P


if __name__ == '__main__':
    P1 = [1, 0, 1]
    P2 = [3, 4]
    X = [0, 1, 2, 3]
    Y1 = naive_polynomial_evaluation(P1, X)
    Y2 = naive_polynomial_evaluation(P2, X)
    Y3 = multiply_values(Y1, Y2)
    P3 = lagrangian_polynomial_interpolation(X, Y3)
    expected = naive_multiplication(P1, P2)

    print(f"P1(X) = {Y1}")
    print(f"P2(X) = {Y2}")
    print(f"P1(X)*P2(X) = {Y3}")
    print(f"P3 = {round_nums(P3)}")
    print(f"Expected = {expected}")
    print(f"P3 as expected? {round_nums(P3) == expected}")

