def round_complex(number, decimal=5):
    return complex(round(number.real, decimal), round(number.imag, decimal))


def round_complex_nums(numbers, decimal=5):
    return [round_complex(number, decimal=decimal) for number in numbers]


def round_real_nums(numbers, decimal=5):
    return [round(number, decimal) for number in numbers]


def round_nums(numbers, decimal=5):
    """
    Only use if input is known to be either all complex or all real, but unsure which
    """
    if isinstance(numbers[0], complex):
        return round_complex_nums(numbers, decimal=decimal)
    else:
        return round_real_nums(numbers, decimal=decimal)

if __name__ == '__main__':
    A = [complex(1,2), 3, 4, complex(6,7)]
    round_nums(A)