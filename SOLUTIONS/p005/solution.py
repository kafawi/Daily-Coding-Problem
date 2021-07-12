def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """Get the first element of the pair.

    >>> car(cons(3, 4))
    3
    """
    return pair(lambda a, b: a)


def cdr(pair):
    """Get the second element of the pair.

    >>> cdr(cons(3, 4))
    4
    """
    return pair(lambda a, b: b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
