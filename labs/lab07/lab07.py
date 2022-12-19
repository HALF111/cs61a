def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # solution 1:
    for item in it:
        yield item *  multiplier
    
    # solution 2, but failed:
    # yield from it


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    # solution 1:
    # while n != 1:
    #     yield n
    #     if n % 2 == 0:
    #         n = n // 2
    #     else:
    #         n = 3 * n + 1
    # yield n

    # solution 2:
    yield n
    if n == 1:
        return
    if n % 2 == 0:
        yield from hailstone(n // 2)
    else:
        yield from hailstone(3 * n + 1)
