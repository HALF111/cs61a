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
# nonlocal and global
doc = "abc"

def changeD(doc):
    # global doc
    # nonlocal doc
    def changeDoc():
        # nonlocal doc
        # doc = doc + "def"
        print(doc)
    return changeDoc


class Account:
    interest = 0.02
    def __init__(self, holder_name) -> None:
        self.balance = 0
        self.holder_name = holder_name
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance


# 2022/12/21
from fractions import Fraction
half = Fraction(1,2)
print(half)
print(repr(half))
print(str(half))
print(eval(repr(half)))
print(eval(str(half)))


class Bear:
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: "this bear"

    def __repr__(self):
        return "Bear()"

    def __str__(self):
        return "a bear"

oski = Bear()
print()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())