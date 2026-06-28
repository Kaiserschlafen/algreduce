import math

from algreduce import is_square, square, cbrt, is_cube, cube, fraction, sqfrac, cbfrac, cubic_root

# solve cubic equation: ax³ + bx² + cx + d = 0
def solve_cubic(a: int, b: int, c: int, d: int) -> dict:
    if a != int(a) or b != int(b) or c != int(c) or d != int(d):
        raise ValueError('a, b, c, d are supposed to be integers!')

    elif a == 0:
        raise ZeroDivisionError('Value \'a\' can\'t be 0!')

    else:
        rational = 36*a*b*c - 108*a**2*d - 8*b**3
        delta = 11664*a**4*d**2 - 432*a**2*b**2*c**2 + 1728*a**2*b**3*d - 7776*a**3*b*c*d + 1728*a**3*c**3

        if b == 0:
            if rational == 0:
                if delta == 0:
                    return {
                        'roots': ['0'],
                        'number of roots': 1,
                        'discriminant': delta
                    }

                else:
                    return {
                        'roots': ['0',
                                  f'{cubic_root(0, -27*delta, 6*a)}',
                                  f'{cubic_root(0, -27*delta, -6*a)}'],
                        'number of roots': 3,
                        'discriminant': delta
                    }

            else:
                if delta > 0:
                    fct = math.gcd(rational, square(delta)[0])
                    rtn = rational // fct
                    dlt = delta // fct ** 2
                    R1 = (rtn ** 2 - dlt) * (rtn + math.sqrt(dlt))
                    R2 = (rtn ** 2 - dlt) * (rtn - math.sqrt(dlt))
                    x = round(rtn/4+3*(cbrt(R1)+cbrt(R2))/8)

                    if is_cube(x):
                        pass

                    else:
                        x = 0

                    R1 = (rational ** 2 - delta) * (rational + math.sqrt(delta))
                    R2 = (rational ** 2 - delta) * (rational - math.sqrt(delta))
                    y = round(rational/4+3*(cbrt(R1)+cbrt(R2))/8)

                    if is_cube(y):
                        pass

                    else:
                        y = 0

                    if x != 0 and is_cube((rtn-x)**3//(27*x)):
                        A = cube(fct)[0] * cube(x)[0]
                        B = cube(fct)[0] ** 2 * (rtn - x) // (3 * cube(x)[0])

                        if if_cube(fct):
                            return {
                                'roots': [f'{fraction(A, 3*a)}',
                                          f'{sqfrac(-A, -3*B, 6*a)}',
                                          f'{sqfrac(-A, -3*B, 6*a, True)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                        else:
                            return {
                                'roots': [f'{fraction(A, 3*a)}·{cubic_root(cube(fct)[1])}',
                                          f'{sqfrac(-A, -3*B, 6*a)}·{cubic_root(cube(fct)[1])}',
                                          f'{sqfrac(-A, -3*B, 6*a, True)}·{cubic_root(cube(fct)[1])}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                    elif y != 0 and is_cube((rational-y)**3//(27*y)):
                        A = cube(y)[0]
                        B = (rational - y) // (3 * cube(y)[0])

                        return {
                            'roots': [f'{fraction(A, 3*a)}',
                                      f'{sqfrac(-A, -3*B, 6*a)}',
                                      f'{sqfrac(-A, -3*B, 6*a, True)}'],
                            'number of roots': 3,
                            'discriminant': delta
                        }

                    else:
                        if is_square(delta):
                            R1 = rational + square(delta)[0]
                            R2 = rational - square(delta)[0]

                            if is_cube(R1):
                                if is_cube(R2):
                                    r1 = cube(R1)[0]
                                    r2 = cube(R2)[0]

                                    return {
                                        'roots': [f'{fraction(r1+r2, 6*a)}',
                                                  f'{sqfrac(-(r1+r2), -3*(r1-r2)**2, 12*a)}',
                                                  f'{sqfrac(-(r1+r2), -3*(r1-r2)**2, 12*a, True)}'],
                                        'number of roots': 3,
                                        'discriminant': delta
                                    }

                                else:
                                    r1 = cube(R1)[0]
                                    num = cube(R2)[0]
                                    rtn = cube(R2)[1]

                                    if R1 == 0:
                                        return {
                                            'roots': [f'{cubic_root(R2, 0, 6*a)}',
                                                      f'{sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                      f'{sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                            'number of roots': 3,
                                            'discriminant': delta
                                        }

                                    else:
                                        if a * R2 > 0:
                                            return {
                                                'roots': [f'{fraction(r1, 6*a)} + {cubic_root(R2, 0, 6*a)}',
                                                          f'{sqfrac(-r1, -3*r1**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-r1, -3*r1**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R2 < 0:
                                            return {
                                                'roots': [f'{fraction(r1, 6*a)} - {cubic_root(R2, 0, -6*a)}',
                                                          f'{sqfrac(-r1, -3*r1**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-r1, -3*r1**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                            else:
                                if is_cube(R2):
                                    r2 = cube(R2)[0]
                                    num = cube(R1)[0]
                                    rtn = cube(R1)[1]

                                    if R2 == 0:
                                        return {
                                            'roots': [f'{cubic_root(R1, 0, 6*a)}',
                                                      f'{sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                      f'{sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                            'number of roots': 3,
                                            'discriminant': delta
                                        }

                                    else:
                                        if a * R1 > 0:
                                            return {
                                                'roots': [f'{fraction(r2, 6*a)} + {cubic_root(R1, 0, 6*a)}',
                                                          f'{sqfrac(-r2, -3*r2**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-r2, -3*r2**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R1 < 0:
                                            return {
                                                'roots': [f'{fraction(r2, 6*a)} - {cubic_root(R1, 0, -6*a)}',
                                                          f'{sqfrac(-r2, -3*r2**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-r2, -3*r2**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                else:
                                    num1 = cube(R1)[0]
                                    rtn1 = cube(R1)[1]
                                    num2 = cube(R2)[0]
                                    rtn2 = cube(R2)[1]

                                    if a * R2 > 0:
                                        return {
                                            'roots': [f'{cubic_root(R1, 0, 6*a)} + {cubic_root(R2, 0, 6*a)}',
                                                      f'{sqfrac(-num1, -3*num1**2, 12*a)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a, True)}·{cubic_root(rtn2)}',
                                                      f'{sqfrac(-num1, -3*num1**2, 12*a, True)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a)}·{cubic_root(rtn2)}'],
                                            'number of roots': 3,
                                            'discriminant': delta
                                        }

                                    if a * R2 < 0:
                                        return {
                                            'roots': [f'{cubic_root(R1, 0, 6*a)} - {cubic_root(R2, 0, -6*a)}',
                                                      f'{sqfrac(-num1, -3*num1**2, 12*a, True)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a)}·{cubic_root(rtn2)}',
                                                      f'{sqfrac(-num1, -3*num1**2, 12*a)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a, True)}·{cubic_root(rtn2)}'],
                                            'number of roots': 3,
                                            'discriminant': delta
                                        }

                        else:
                            fct = math.gcd(rational, square(delta)[0])
                            rtn = rational // fct
                            dlt = delta // fct ** 2
                            num = cube(fct)[0]

                            if a > 0:
                                return {
                                    'roots': [f'{cubic_root(rational, delta, 6*a)} + {cubic_root(rational, delta, 6*a, True)}',
                                              f'{sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}',
                                              f'{sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                            elif a < 0:
                                return {
                                    'roots': [f'{cubic_root(rational, delta, 6*a)} - {cubic_root(rational, delta, -6*a, True)}',
                                              f'{sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}',
                                              f'{sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                elif delta < 0:
                    fct = math.gcd(rational, square(-delta)[0])
                    rtn = rational // fct
                    dlt = delta // fct ** 2
                    theta = math.atan(math.sqrt(-dlt)/abs(rtn))
                    z1 = round(abs(rtn)/4+3*math.sqrt(rtn**2-dlt)*math.cos(theta/3)/4)
                    z2 = round(abs(rtn)/4+3*math.sqrt(rtn**2-dlt)*math.cos(theta/3+2*math.pi/3)/4)
                    z3 = round(abs(rtn)/4+3*math.sqrt(rtn**2-dlt)*math.cos(theta/3+4*math.pi/3)/4)

                    if is_cube(z1):
                        x = z1

                    elif is_cube(z2):
                        x = z2

                    elif is_cube(z3):
                        x = z3

                    else:
                        x = 0

                    theta = math.atan(math.sqrt(-delta)/abs(rational))
                    z1 = round(abs(rational)/4+3*math.sqrt(rational**2-delta)*math.cos(theta/3)/4)
                    z2 = round(abs(rational)/4+3*math.sqrt(rational**2-delta)*math.cos(theta/3+2*math.pi/3)/4)
                    z3 = round(abs(rational)/4+3*math.sqrt(rational**2-delta)*math.cos(theta/3+4*math.pi/3)/4)

                    if is_cube(z1):
                        y = z1

                    elif is_cube(z2):
                        y = z2

                    elif is_cube(z3):
                        y = z3

                    else:
                        y = 0

                    if rational < 0:
                        x = -x
                        y = -y

                    else:
                        pass

                    if x != 0 and is_cube((x-rtn)**3//(27*x)):
                        A = cube(fct)[0] * cube(x)[0]
                        B = cube(fct)[0] ** 2 * (x - rtn) // (3 * cube(x)[0])

                        if is_cube(fct):
                            if is_square(3*B):
                                return {
                                    'roots': [f'{fraction(A, 3*a)}',
                                              f'{fraction(-A+square(3*B)[0], 6*a)}',
                                              f'{fraction(-A-square(3*B)[0], 6*a)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                            else:
                                return {
                                    'roots': [f'{fraction(A, 3*a)}',
                                              f'{sqfrac(-A, 3*B, 6*a)}',
                                              f'{sqfrac(-A, 3*B, 6*a, True)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                        else:
                            if is_square(3*B):
                                return {
                                    'roots': [f'{fraction(A, 3*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{fraction(-A+square(3*B)[0], 6*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{fraction(-A-square(3*B)[0], 6*a)}·{cubic_root(cube(fct)[1])}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                            else:
                                return {
                                    'roots': [f'{fraction(A, 3*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{sqfrac(-A, 3*B, 6*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{sqfrac(-A, 3*B, 6*a, True)}·{cubic_root(cube(fct)[1])}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                    elif y != 0 and is_cube((y-rational)**3//(27*y)):
                        A = cube(y)[0]
                        B = (y - rational) // (3 * cube(y)[0])

                        if is_square(3*B):
                            return {
                                'roots': [f'{fraction(A, 3*a)}',
                                          f'{fraction(-A+square(3*B)[0], 6*a)}',
                                          f'{fraction(-A-square(3*B)[0], 6*a)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                        else:
                            return {
                                'roots': [f'{fraction(A, 3*a)}',
                                          f'{sqfrac(-A, 3*B, 6*a)}',
                                          f'{sqfrac(-A, 3*B, 6*a, True)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                    else:
                        fct = math.gcd(rational, square(-delta)[0])
                        rtn = rational // fct
                        dlt = delta // fct ** 2
                        num = cube(fct)[0]

                        if a > 0:
                            return {
                                'roots': [f'{cubic_root(rational, delta, 6*a)} + {cubic_root(rational, delta, 6*a, True)}',
                                          f'{sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}',
                                          f'{sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                        elif a < 0:
                            return {
                                'roots': [f'{cubic_root(rational, delta, 6*a)} - {cubic_root(rational, delta, -6*a, True)}',
                                          f'{sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}',
                                          f'{sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                else:
                    return {
                        'roots': [f'{cubic_root(rational, 0, 3*a)}',
                                  f'{cubic_root(rational, 0, -6*a)}'],
                        'number of roots': 2,
                        'discriminant': delta
                    }

        else:
            if rational == 0:
                if delta > 0:
                    return {
                        'roots': [f'{fraction(-b, 3*a)}',
                                  f'{fraction(-b, 3*a)} + {cubic_root(0, -27*delta, -abs(6*a))}',
                                  f'{fraction(-b, 3*a)} - {cubic_root(0, -27*delta, -abs(6*a))}'],
                        'number of roots': 3,
                        'discriminant': delta
                    }

                elif delta < 0:
                    return {
                        'roots': [f'{fraction(-b, 3*a)}',
                                  f'{fraction(-b, 3*a)} + {cubic_root(0, -27*delta, abs(6*a))}',
                                  f'{fraction(-b, 3*a)} - {cubic_root(0, -27*delta, abs(6*a))}'],
                        'number of roots': 3,
                        'discriminant': delta
                    }

                else:
                    return {
                        'roots': [f'{fraction(-b, 3*a)}'],
                        'number of roots': 1,
                        'discriminant': delta
                    }

            else:
                if delta > 0:
                    fct = math.gcd(rational, square(delta)[0])
                    rtn = rational // fct
                    dlt = delta // fct ** 2
                    R1 = (rtn ** 2 - dlt) * (rtn + math.sqrt(dlt))
                    R2 = (rtn ** 2 - dlt) * (rtn - math.sqrt(dlt))
                    x = round(rtn/4+3*(cbrt(R1)+cbrt(R2))/8)

                    if is_cube(x):
                        pass

                    else:
                        x = 0

                    R1 = (rational ** 2 - delta) * (rational + math.sqrt(delta))
                    R2 = (rational ** 2 - delta) * (rational - math.sqrt(delta))
                    y = round(rational/4+3*(cbrt(R1)+cbrt(R2))/8)

                    if is_cube(y):
                        pass

                    else:
                        y = 0

                    if x != 0 and is_cube((rtn-x)**3//(27*x)):
                        A = cube(fct)[0] * cube(x)[0]
                        B = cube(fct)[0] ** 2 * (rtn - x) // (3 * cube(x)[0])

                        if is_cube(fct):
                            return {
                                'roots': [f'{fraction(-b+A, 3*a)}',
                                          f'{sqfrac(-2*b-A, -3*B, 6*a)}',
                                          f'{sqfrac(-2*b-A, -3*B, 6*a, True)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                        else:
                            return {
                                'roots': [f'{fraction(-b+A, 3*a)}·{cubic_root(cube(fct)[1])}',
                                          f'{sqfrac(-2*b-A, -3*B, 6*a)}·{cubic_root(cube(fct)[1])}',
                                          f'{sqfrac(-2*b-A, -3*B, 6*a, True)}·{cubic_root(cube(fct)[1])}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                    elif y != 0 and is_cube((rational-y)**3//(27*y)):
                        A = cube(y)[0]
                        B = (rational - y) // (3 * cube(y)[0])

                        return {
                            'roots': [f'{fraction(-b+A, 3*a)}',
                                      f'{sqfrac(-2*b-A, -3*B, 6*a)}',
                                      f'{sqfrac(-2*b-A, -3*B, 6*a, True)}'],
                            'number of roots': 3,
                            'discriminant': delta
                        }

                    else:
                        if is_square(delta):
                            R1 = rational + square(delta)[0]
                            R2 = rational - square(delta)[0]

                            if is_cube(R1):
                                if is_cube(R2):
                                    r1 = cube(R1)[0]
                                    r2 = cube(R2)[0]

                                    return {
                                        'roots': [f'{fraction(-2*b+r1+r2, 6*a)}',
                                                  f'{sqfrac(-4*b-(r1+r2), -3*(r1-r2)**2, 12*a)}',
                                                  f'{sqfrac(-4*b-(r1+r2), -3*(r1-r2)**2, 12*a, True)}'],
                                        'number of roots': 3,
                                        'discriminant': delta
                                    }

                                else:
                                    r1 = cube(R1)[0]
                                    num = cube(R2)[0]
                                    rtn = cube(R2)[1]

                                    if R1 == 0:
                                        if a * R2 > 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} + {cubic_root(R2, 0, 6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R2 < 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} - {cubic_root(R2, 0, -6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                    else:
                                        if a * R2 > 0:
                                            return {
                                                'roots': [f'{fraction(-2*b+r1, 6*a)} + {cubic_root(R2, 0, 6*a)}',
                                                          f'{sqfrac(-4*b-r1, -3*r1**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-4*b-r1, -3*r1**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R2 < 0:
                                            return {
                                                'roots': [f'{fraction(-2*b+r1, 6*a)} - {cubic_root(R2, 0, -6*a)}',
                                                          f'{sqfrac(-4*b-r1, -3*r1**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-4*b-r1, -3*r1**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                            else:
                                if is_cube(R2):
                                    r2 = cube(R2)[0]
                                    num = cube(R1)[0]
                                    rtn = cube(R1)[1]

                                    if R2 == 0:
                                        if a * R1 > 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} + {cubic_root(R1, 0, 6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R1 < 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} - {cubic_root(R1, 0, -6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                    else:
                                        if a * R1 > 0:
                                            return {
                                                'roots': [f'{fraction(-2*b+r2, 6*a)} + {cubic_root(R1, 0, 6*a)}',
                                                          f'{sqfrac(-4*b-r2, -3*r2**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-4*b-r2, -3*r2**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R1 < 0:
                                            return {
                                                'roots': [f'{fraction(-2*b+r2, 6*a)} - {cubic_root(R1, 0, -6*a)}',
                                                          f'{sqfrac(-4*b-r2, -3*r2**2, 12*a, True)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn)}',
                                                          f'{sqfrac(-4*b-r2, -3*r2**2, 12*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                else:
                                    num1 = cubc(R1)[0]
                                    rtn1 = cube(R1)[1]
                                    num2 = cube(R2)[0]
                                    rtn2 = cube(R2)[1]

                                    if a * R1 > 0:
                                        if a * R2 > 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} + {cubic_root(R1, 0, 6*a)} + {cubic_root(R2, 0, 6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a, True)}·{cubic_root(rtn2)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a, True)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a)}·{cubic_root(rtn2)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R2 < 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} + {cubic_root(R1, 0, 6*a)} - {cubic_root(R2, 0, -6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a, True)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a)}·{cubic_root(rtn2)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a, True)}·{cubic_root(rtn2)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                    elif a * R1 < 0:
                                        if a * R2 > 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} - {cubic_root(R1, 0, 6*a)} + {cubic_root(R2, 0, 6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a, True)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a)}·{cubic_root(rtn2)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a, True)}·{cubic_root(rtn2)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                                        elif a * R2 < 0:
                                            return {
                                                'roots': [f'{fraction(-b, 3*a)} - {cubic_root(R1, 0, 6*a)} - {cubic_root(R2, 0, -6*a)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a, True)}·{cubic_root(rtn2)}',
                                                          f'{fraction(-b, 3*a)} + {sqfrac(-num1, -3*num1**2, 12*a, True)}·{cubic_root(rtn1)} + {sqfrac(-num2, -3*num2**2, 12*a)}·{cubic_root(rtn2)}'],
                                                'number of roots': 3,
                                                'discriminant': delta
                                            }

                        else:
                            fct = math.gcd(rational, square(delta)[0])
                            rtn = rational // fct
                            dlt = delta // fct ** 2
                            num = cube(fct)[0]

                            if a > 0:
                                return {
                                    'roots': [f'{fraction(-b, 3*a)} + {cubic_root(rational, delta, 6*a)} + {cubic_root(rational, delta, 6*a, True)}',
                                              f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}',
                                              f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                            elif a < 0:
                                return {
                                    'roots': [f'{fraction(-b, 3*a)} - {cubic_root(rational, delta, -6*a)} - {cubic_root(rational, delta, -6*a, True)}',
                                              f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}',
                                              f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                elif delta < 0:
                    fct = math.gcd(rational, square(-delta)[0])
                    rtn = rational // fct
                    dlt = delta // fct ** 2
                    theta = math.atan(math.sqrt(-dlt)/abs(rtn))
                    z1 = round(abs(rtn)/4+3*math.sqrt(rtn**2-dlt)*math.cos(theta/3)/4)
                    z2 = round(abs(rtn)/4+3*math.sqrt(rtn**2-dlt)*math.cos(theta/3+2*math.pi/3)/4)
                    z3 = round(abs(rtn)/4+3*math.sqrt(rtn**2-dlt)*math.cos(theta/3+4*math.pi/3)/4)

                    if is_cube(z1):
                        x = z1

                    elif is_cube(z2):
                        x = z2

                    elif is_cube(z3):
                        x = z3

                    else:
                        x = 0

                    theta = math.atan(math.sqrt(-delta)/abs(rational))
                    z1 = round(abs(rational)/4+3*math.sqrt(rational**2-delta)*math.cos(theta/3)/4)
                    z2 = round(abs(rational)/4+3*math.sqrt(rational**2-delta)*math.cos(theta/3+2*math.pi/3)/4)
                    z3 = round(abs(rational)/4+3*math.sqrt(rational**2-delta)*math.cos(theta/3+4*math.pi/3)/4)

                    if is_cube(z1):
                        y = z1

                    elif is_cube(z2):
                        y = z2

                    elif is_cube(z3):
                        y = z3

                    else:
                        y = 0

                    if rational < 0:
                        x = -x
                        y = -y

                    else:
                        pass

                    if x != 0 and is_cube((x-rtn)**3//(27*x)):
                        A = cube(fct)[0] * cube(x)[0]
                        B = cube(fct)[0] ** 2 * (x - rtn) // (3 * cube(x)[0])

                        if is_cube(fct):
                            if is_square(3*B):
                                return {
                                    'roots': [f'{fraction(-b+A, 3*a)}',
                                              f'{fraction(-2*b-A+square(3*B)[0], 6*a)}',
                                              f'{fraction(-2*b-A-square(3*B)[0], 6*a)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                            else:
                                return {
                                    'roots': [f'{fraction(-b+A, 3*a)}',
                                              f'{sqfrac(-2*b-A, 3*B, 6*a)}',
                                              f'{sqfrac(-2*b-A, 3*B, 6*a, True)}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                        else:
                            if is_square(3*B):
                                return {
                                    'roots': [f'{fraction(-b+A, 3*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{fraction(-2*b-A+square(3*B)[0], 6*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{fraction(-2*b-A-square(3*B)[0], 6*a)}·{cubic_root(cube(fct)[1])}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                            else:
                                return {
                                    'roots': [f'{fraction(-b+A, 3*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{sqfrac(-2*b-A, 3*B, 6*a)}·{cubic_root(cube(fct)[1])}',
                                              f'{sqfrac(-2*b-A, 3*B, 6*a, True)}·{cubic_root(cube(fct)[1])}'],
                                    'number of roots': 3,
                                    'discriminant': delta
                                }

                    if y != 0 and is_cube((y-rational)**3//(27*y)):
                        A = cube(y)[0]
                        B = (y - rational) // (3 * cube(y)[0])

                        if is_square(3*B):
                            return {
                                'roots': [f'{fraction(-b+A, 3*a)}',
                                          f'{fraction(-2*b-A+square(3*B)[0], 6*a)}',
                                          f'{fraction(-2*b-A-square(3*B)[0], 6*a)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                        else:
                            return {
                                'roots': [f'{fraction(-b+A, 3*a)}',
                                          f'{sqfrac(-2*b-A, 3*B, 6*a)}',
                                          f'{sqfrac(-2*b-A, 3*B, 6*a, True)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                    else:
                        fct = math.gcd(rational, square(-delta)[0])
                        rtn = rational // fct
                        dlt = delta // fct ** 2
                        num = cube(fct)[0]

                        if a > 0:
                            return {
                                'roots': [f'{fraction(-b, 3*a)} + {cubic_root(rational, delta, 6*a)} + {cubic_root(rational, delta, 6*a, True)}',
                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}',
                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                        elif a < 0:
                            return {
                                'roots': [f'{fraction(-b, 3*a)} - {cubic_root(rational, delta, -6*a)} - {cubic_root(rational, delta, -6*a, True)}',
                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)}',
                                          f'{fraction(-b, 3*a)} + {sqfrac(-num, -3*num**2, 12*a)}·{cubic_root(rtn, dlt)} + {sqfrac(-num, -3*num**2, 12*a, True)}·{cubic_root(rtn, dlt)}'],
                                'number of roots': 3,
                                'discriminant': delta
                            }

                else:
                    if is_cube(rational):
                        return {
                            'roots': [f'{fraction(-b+round(cbrt(rational)), 3*a)}',
                                      f'{fraction(-2*b-round(cbrt(rational)), 6*a)}'],
                            'number of roots': 2,
                            'discriminant': delta
                        }

                    else:
                        if a * rational > 0:
                            return {
                                'roots': [f'{fraction(-b, 3*a)} + {cubic_root(rational, 0, 3*a)}',
                                          f'{fraction(-b, 3*a)} - {cubic_root(rational, 0, 6*a)}'],
                                'number of roots': 2,
                                'discriminant': delta
                            }

                        elif a * rational < 0:
                            return {
                                'roots': [f'{fraction(-b, 3*a)} - {cubic_root(rational, 0, -3*a)}',
                                          f'{fraction(-b, 3*a)} + {cubic_root(rational, 0, -6*a)}'],
                                'number of roots': 2,
                                'discriminant': delta
                            }
