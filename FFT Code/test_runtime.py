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

def save_data_to_csv(function, label, data):
    """function: used to get the name of the test function as the title of the file,
    label: string to specify which algorithm the data is from,
    data: a 2D array of all the output from the testing
    This function will parse data and save it to a text file in CSV format. """

    unique_stamp = dt.now().strftime('%H%M%S%f') # so each run of the test has its own file
    file_name = f"{function.__name__}_{label}_{unique_stamp}"
    file_path = "Output/" + file_name + ".txt"
    with open(file_path, 'w+') as f:
        for i in range(len(data)): # each row
            for j in range(len(data[0])):  # each column
                f.write(f"{data[i][j]}") # record each piece of data
                if j != len(data[0]) - 1: # no comma on end of line
                    f.write(",")
            f.write("\n") # new line for each test iteration's data
        print(f"Successfully saved data to {file_path}")


if __name__ == '__main__':
    test_timing(naive_multiplication)
    test_timing(FFT_multiplication())

