import math

from algreduce import is_square, square, fraction, sqfrac

# solve quadratic equation: ax² + bx + c = 0
def solve_quadratic(a: int, b: int, c: int) -> dict:
    if a != int(a) or b != int(b) or c != int(c):
        raise ValueError('a, b, c are supposed to be integers!')

    elif a == 0:
        raise ZeroDivisionError('Value \'a\' can\'t be 0!')

    else:
        delta = b**2 - 4*a*c

        if b == 0:
            if delta == 0:
                return {
                    'roots': ['0'],
                    'number of roots': 1,
                    'discriminants': delta,
                    'is_complex': delta < 0
                }

            else:
                return {
                    'roots': [f'{sqfrac(0, delta, 2*a)}', f'{sqfrac(0, delta, 2*a, True)}'],
                    'number of roots': 2,
                    'discriminants': delta,
                    'is_complex': delta < 0
                }

        else:
            if delta == 0:
                return {
                    'roots': [f'{sqfrac(-b, 0, 2*a)}'],
                    'number of roots': 1,
                    'discriminants': delta,
                    'is_complex': delta < 0
                }

            else:
                return {
                    'roots': [f'{sqfrac(-b, delta, 2*a)}', f'{sqfrac(-b, delta, 2*a, True)}'],
                    'number of roots': 2,
                    'discriminants': delta,
                    'is_complex': delta < 0
                }
