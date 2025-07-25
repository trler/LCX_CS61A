"""Our first python source file."""
from operator import floordiv, mod

def divide_exact(n,d=10):
    """Return the quotient and remainder of n divided by d.
    >>> q,r = divide_exact(2013,10)
    >>> q
    201
    >>> r
    2
    """

    return floordiv(n,d), mod(n,d)



def adsulute_value(x):
    """Return the absolute value of x.
    >>> adsulute_value(-10)
    10
    >>> adsulute_value(10)
    10
    """
    if x < 0:
        return -x
    else:
        return x

