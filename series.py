def fibonacci(n):
    """
    The Fibonacci Series is a numeric
    series starting with the integers 0 and 1.
     In this series, the next integer is
     determined by summing the previous two.
    """
    if n in {0, 1}:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


def lucas(n):
    """
    The Lucas Numbers are a related
    series of integers that start with
    the values 2 and 1 rather than 0 and 1.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):
    """
    Takes in one required parameter and two optional.
    Calling this function with no optional parameters
    will produce numbers from the fibonacci series.
    Calling it with the optional arguments 2 and 1
    will produce values from the lucas numbers.
    Other values for the optional parameters will
    produce other series
    """
    if n == 0:
        return first
    if n == 1:
        return second
    else:
        return sum_series((n - 1), first, second) + sum_series((n - 2), first, second)