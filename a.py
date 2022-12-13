def f(n, d):
    """asddsad

    >>> q, r = f(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return n // d, n % d

def a():
    print("a")
    return "aaa"

def b():
    print("b")
    return "bbb"


# 2022/12/12
doc = "abc"

def changeD(doc):
    # global doc
    # nonlocal doc
    def changeDoc():
        # nonlocal doc
        # doc = doc + "def"
        print(doc)
    return changeDoc
