def two_chip_extra(numbers, X):
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    return None, None
