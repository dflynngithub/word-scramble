# ./scrmabled-strings

def char_to_ord(c: str) -> int:
    """
    Converts a character `c` to an integer value as in the ASCII table.
    This wraps around the basic function "ord" to catch exceptions.
    """
    # Make sure that c is valid and return the ordinal value for c
    if len(c) != 1:
        raise Exception("Must provide a single character")
    else:
        return ord(c)


def ord_to_char(n: int) -> str:
    """
    Converts an integer `n` to a character value as in the ASCII table.
    This wraps around the basic function "chr" to catch exceptions.
    """
    # First make sure that n is valid
    if n < 97 or n > 122:
        raise Exception("Must provide an ordinal value that maps to [a,z]")
    else:
        return chr(n)


def ord_recurrence(x1: int, x2: int, A: int, B: int, C: int, D: int) -> int:
    """
    Generates the next ordinal value xi in a word by recurrence.
    """
    # Raise exceptions for invalide choices of parameters
    if A < 0 or A > 10**9:
        raise Exception("The parameter A must satisfy 0 <= A <= 10^9.")
    if B < 0 or B > 10**9:
        raise Exception("The parameter B must satisfy 0 <= B <= 10^9.")
    if C < 0 or C > 10**9:
        raise Exception("The parameter C must satisfy 0 <= C <= 10^9.")
    if D < 1 or D > 10**9:
        raise Exception("The parameter D must satisfy 1 <= D <= 10^9.")

    # Do a little bit of modular arithmetic
    return ((A*x1 + B*x2 + C) % D)


def char_recurrence(x: int) -> str:
    """
    Generates a character Si from ordinal xi a recurrence relation.
    Valid for all i = 3 to N.
    """

    # Do a little bit of modular arithmetic
    return (ord_to_char(97 + (x % 26)))


print(char_recurrence(ord_recurrence(97, 99, 1, 1, 1, 2)))
