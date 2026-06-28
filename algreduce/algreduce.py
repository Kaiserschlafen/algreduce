import math

# determine whether a radicand is a perfect square
def is_square(radicand: int) -> bool:
    return round(math.sqrt(radicand)) ** 2 == radicand

# simplify squares: √r -> a√b
def square(radicand: int) -> tuple:
    """
    return:
        tuple (a, b)

    examples:
        >>>square(4)
        (2, 1)
        >>>square(8)
        (2, 2)
        >>>square(5)
        (1, 5)
        >>>square(48)
        (4, 3)
    """
    if is_square(radicand):
        a = round(math.sqrt(radicand))
        b = 1

    else:
        b = 2

        while not is_square(radicand/b):
            b += 1

        a = round(math.sqrt(radicand/b))

    return (a, b)

# calculate the cubic root of radicands
def cbrt(radicand: float) -> float:
    if radicand >= 0:
        return math.pow(radicand, 1/3)

    elif radicand < 0:
        return -math.pow(-radicand, 1/3)

# determine whether a radicand is a perfect cube
def is_cube(radicand: int) -> bool:
    return round(cbrt(radicand)) ** 3 == radicand

# simplify cubes: ³√r -> a·³√b
def cube(radicand: int) -> tuple:
    """
    return:
        tuple (a, b)

    examples:
        >>>cube(8)
        (2, 1)
        >>>cube(18)
        (1, 18)
        >>>cube(-9)
        (-1, 9)
        >>>cube(24)
        (2, 3)
    """
    if is_cube(radicand):
        a = round(cbrt(radicand))
        b = 1

    else:
        b = 2

        while not is_cube(radicand/b):
            b += 1

        a = round(cbrt(radicand/b))

    return (a, b)

# simplify fractions
def fraction(numerator: int, denominator: int) -> str:
    """
    simplify and format mathematical expressions as strings

    parameters:
        numerator: the numerator of the fraction
        denominator: the denominator of the fraction

    return:
        formatted string of the mathematical expression

    examples:
        >>>fraction(5, 7)
        '5/7'
        >>>fraction(10, 4)
        '5/2'
        >>>fraction(3, 9)
        '1/3'
        >>>fraction(8, 2)
        '4'
    """
    # special cases for 0
    if numerator == 0 and denominator != 0:
        return '0'

    elif numerator != 0 and denominator == 0:
        return '∞'

    elif numerator == 0 and denominator == 0:
        return '0/0'

    else:
        # simplify the fraction into reduced fraction
        gcd = math.gcd(numerator, denominator)
        num = numerator // gcd
        den = denominator // gcd

        # n/1 -> n
        if den == 1:
            return f'{num}'

        # n/-1 -> -n
        elif den == -1:
            return f'{-num}'

        # n/d -> n/|d|
        elif den > 0:
            return f'{num}/{den}'

        # n/d -> -n/|d|
        elif den < 0:
            return f'{-num}/{-den}'

# simplify fractions contain square root
def sqfrac(rational: int, radicand: int, denominator: int, is_minus: bool=False) -> str:
    """
    simplify and format fractions with square root

    parameters:
        rational: the integer in numerator of the fraction
        radicand: the radicand in numerator of the fraction
        denominator: the denominator of the fraction
        is_minus: change the '+' between rational and radicand into '-' (default as False)

    return:
        formatted string of the mathematical expression

    examples:
        >>>sqfrac(2, 3, 1)
        '2+√3'
        >>>sqfrac(1, 9, 1)
        '4'
        >>>sqfrac(3, 8, 3, True)
        '(3-2√2)/3'
        >>>sqfrac(1, 0, 2)
        '1/2'
        >>>sqfrac(0, -4, 2, True)
        '-i'
    """
    # format the reduced fraction
    def formal(expression: str) -> str:
        if cef == 1:
            # 1√1/den -> 1/den
            if rdc == 1:
                if radicand < 0:
                    expression = expression.replace('1√1', '')

                else:
                    expression = expression.replace('√1', '')

            # 1√rdc/den -> √rdc/den
            else:
                expression = expression.replace('1√', '√')

        else:
            # cef√1/den -> cef/den
            if rdc == 1:
                expression = expression.replace('√1', '')

            # cef√rdc/den
            else:
                pass

        return expression

    # ± √radicand / denominator
    if rational == 0:
        # fraction is a real number
        if radicand > 0:
            rdc = square(radicand)[1]
            gcd = math.gcd(square(radicand)[0], denominator)
            cef = square(radicand)[0] // gcd
            den = denominator // gcd

            if den == 1:
                if is_minus:
                    return formal(f'{-cef}√{rdc}')

                else:
                    return formal(f'{cef}√{rdc}')

            elif den == -1:
                if is_minus:
                    return formal(f'{cef}√{rdc}')

                else:
                    return formal(f'{-cef}√{rdc}')

            elif den > 0:
                if is_minus:
                    return formal(f'{-cef}√{rdc}/{den}')

                else:
                    return formal(f'{cef}√{rdc}/{den}')

            elif den < 0:
                if is_minus:
                    return formal(f'{cef}√{rdc}/{-den}')

                else:
                    return formal(f'{-cef}√{rdc}/{-den}')

        # fraction is a complex number
        elif radicand < 0:
            rdc = square(-radicand)[1]
            gcd = math.gcd(square(-radicand)[0], denominator)
            cef = square(-radicand)[0] // gcd
            den = denominator // gcd

            if den == 1:
                if is_minus:
                    return formal(f'{-cef}√{rdc}i')

                else:
                    return formal(f'{cef}√{rdc}i')

            elif den == -1:
                if is_minus:
                    return formal(f'{cef}√{rdc}i')

                else:
                    return formal(f'{-cef}√{rdc}i')

            elif den > 0:
                if is_minus:
                    return formal(f'{-cef}√{rdc}i/{den}')

                else:
                    return formal(f'{cef}√{rdc}i/{den}')

            elif den < 0:
                if is_minus:
                    return formal(f'{cef}√{rdc}i/{-den}')

                else:
                    return formal(f'{-cef}√{rdc}i/{-den}')

        # case for 0
        else:
            return '0'

    # (rational ± √radicand) / denominator
    else:
        # fraction is a real number
        if radicand > 0:
            # num / den
            if is_square(radicand):
                if is_minus:
                    numerator = rational - square(radicand)[0]

                else:
                    numerator = rational + square(radicand)[0]

                return fraction(numerator, denominator)

            # (rtn ± √rdc) / den
            else:
                fct = math.gcd(rational, square(radicand)[0])
                gcd = math.gcd(fct, denominator)
                rtn = rational // gcd
                cef = square(radicand)[0] // gcd
                rdc = square(radicand)[1]
                den = denominator // gcd

                if den == 1:
                    if is_minus:
                        return formal(f'{rtn}-{cef}√{rdc}')

                    else:
                        return formal(f'{rtn}+{cef}√{rdc}')

                elif den == -1:
                    if is_minus:
                        return formal(f'{-rtn}+{cef}√{rdc}')

                    else:
                        return formal(f'{-rtn}-{cef}√{rdc}')

                elif den > 0:
                    if is_minus:
                        return formal(f'({rtn}-{cef}√{rdc})/{den}')

                    else:
                        return formal(f'({rtn}+{cef}√{rdc})/{den}')

                elif den < 0:
                    if is_minus:
                        return formal(f'({-rtn}+{cef}√{rdc})/{-den}')

                    else:
                        return formal(f'({-rtn}-{cef}√{rdc})/{-den}')

        # fraction is a complex number
        elif radicand < 0:
            fct = math.gcd(rational, square(-radicand)[0])
            gcd = math.gcd(fct, denominator)
            rtn = rational // gcd
            cef = square(-radicand)[0] // gcd
            rdc = square(-radicand)[1]
            den = denominator // gcd

            if den == 1:
                if is_minus:
                    return formal(f'{rtn}-{cef}√{rdc}i')

                else:
                    return formal(f'{rtn}+{cef}√{rdc}i')

            elif den == -1:
                if is_minus:
                    return formal(f'{-rtn}+{cef}√{rdc}i')

                else:
                    return formal(f'{-rtn}-{cef}√{rdc}i')

            elif den > 0:
                if is_minus:
                    return formal(f'({rtn}-{cef}√{rdc}i)/{den}')

                else:
                    return formal(f'({rtn}+{cef}√{rdc}i)/{den}')

            elif den < 0:
                if is_minus:
                    return formal(f'({-rtn}+{cef}√{rdc}i)/{-den}')

                else:
                    return formal(f'({-rtn}-{cef}√{rdc}i)/{-den}')

        # rational / denominator
        else:
            return fraction(rational, denominator)

# simplify fractions contain cubic root which contains square root
def cbfrac(rational: int, radicand: int, denominator: int, is_minus: bool=False) -> str:
    """
    simplify fractions with cubic root

    parameters:
        rational: the integer in numerator of the fraction
        radicand: the radicand in numerator of the fraction
        denominator: the denominator of the fraction
        is_minus: change the '+' between rational and radicand into '-' (default as False)

    return:
        formatted string of the mathematical expression

    examples:
        >>>cbfrac(3, 5, 1)
        '³√(3+√5)'
        >>>cbfrac(15, 1, 2)
        '³√2'
        >>>cbfrac(0, -3, 3)
        '-⁶√3i/3'
        >>>cbfrac(9, 1, 5, True)
        '2/5'
        >>>cbfrac(7, -4, 3, True)
        '³√(7-2i)/3'
    """
    # format the cubic root
    def sformal(expression: str) -> str:
        if num == 1 or num == -1:
            # 1·³√1/den -> 1/den, 1·⁶√1/den -> 1/den
            if rdc == 1:
                if radicand < 0:
                    expression = expression.replace('1·³√1', '').replace('1·⁶√1', '')

                else:
                    expression = expression.replace('·³√1', '').replace('·⁶√1', '')

            # 1·³√rdc/den -> ³√rdc/den, 1·⁶√rdc/den -> ⁶√rdc/den
            else:
                expression = expression.replace('1·³√', '³√').replace('1·⁶√', '⁶√')

        else:
            # num·³√1/den -> num/den, num·⁶√1/den -> num/den
            if rdc == 1:
                expression = expression.replace('·³√1', '').replace('·⁶√1', '')

            # num·³√rdc/den, num·⁶√rdc/den
            else:
                pass

        return expression

    # format the cubic root and square root
    def cformal(expression: str) -> str:
        # 1·³√rdc/den -> ³√rdc/den, 1·⁶√rdc/den -> ⁶√rdc/den
        if num == 1 or num == -1:
            expression = expression.replace('1·³√', '³√')

        if cef == 1:
            # rtn ± 1√1 -> rtn ± 1
            if rdc == 1:
                if radicand < 0:
                    expression = expression.replace('1√1', '')

                else:
                    expression = expression.replace('1√1', '1')

            # rtn ± 1√rdc -> rtn ± √rdc
            else:
                expression = expression.replace('1√', '√')

        else:
            # rtn ± cef√1 -> rtn ± cef
            if rdc == 1:
                expression = expression.replace(f'{cef}√1', f'{cef}')

            # rtn ± cef√rdc
            else:
                pass

        return expression

    # ± ⁶√radicand / denominator
    if rational == 0:
        # fraction is a real number
        if radicand > 0:
            if is_minus:
                fct = -square(radicand)[0]

            else:
                fct = square(radicand)[0]

            # num·³√rdc / den
            if is_square(radicand):
                rdc = cube(fct)[1]
                gcd = math.gcd(cube(fct)[0], denominator)
                num = cube(fct)[0] // gcd
                den = denominator // gcd

                if den == 1:
                    return sformal(f'{num}·³√{rdc}')

                elif den == -1:
                    return sformal(f'{-num}·³√{rdc}')

                elif den > 0:
                    return sformal(f'{num}·³√{rdc}/{den}')

                elif den < 0:
                    return sformal(f'{-num}·³√{rdc}/{-den}')

            # num·⁶√rdc / den
            else:
                rdc = square(radicand)[1] * cube(fct)[1] ** 2
                gcd = math.gcd(cube(fct)[0], denominator)
                num = cube(fct)[0] // gcd
                den = denominator // gcd

                if den == 1:
                    return sformal(f'{num}·⁶√{rdc}')

                elif den == -1:
                    return sformal(f'{-num}·⁶√{rdc}')

                elif den > 0:
                    return sformal(f'{num}·⁶√{rdc}/{den}')

                elif den < 0:
                    return sformal(f'{-num}·⁶√{rdc}/{-den}')

        # fraction is a complex number
        if radicand < 0:
            if is_minus:
                fct = square(-radicand)[0]

            else:
                fct = -square(-radicand)[0]

            # num·³√rdc*i / den
            if is_square(-radicand):
                rdc = cube(fct)[1]
                gcd = math.gcd(cube(fct)[0], denominator)
                num = cube(fct)[0] // gcd
                den = denominator // gcd

                if den == 1:
                    return sformal(f'{num}·³√{rdc}i')

                elif den == -1:
                    return sformal(f'{-num}·³√{rdc}i')

                elif den > 0:
                    return sformal(f'{num}·³√{rdc}i/{den}')

                elif den < 0:
                    return sformal(f'{-num}·³√{rdc}i/{-den}')

            # num·⁶√rdc*i / den
            else:
                rdc = square(-radicand)[1] * cube(fct)[1] ** 2
                gcd = math.gcd(cube(fct)[0], denominator)
                num = cube(fct)[0] // gcd
                den = denominator // gcd

                if den == 1:
                    return sformal(f'{num}·⁶√{rdc}i')

                elif den == -1:
                    return sformal(f'{-num}·⁶√{rdc}i')

                elif den > 0:
                    return sformal(f'{num}·⁶√{rdc}i/{den}')

                elif den < 0:
                    return sformal(f'{-num}·⁶√{rdc}i/{-den}')

        # case for 0
        else:
            return '0'

    # ³√(rational ± √radicand) / denominator
    else:
        # fraction is a real number
        if radicand > 0:
            # num·³√rdc / den
            if is_square(radicand):
                if is_minus:
                    rtn = rational - square(radicand)[0]

                else:
                    rtn = rational + square(radicand)[0]

                rdc = cube(rtn)[1]
                gcd = math.gcd(cube(rtn)[0], denominator)
                num = cube(rtn)[0] // gcd
                den = denominator // gcd

                if den == 1:
                    return sformal(f'{num}·³√{rdc}')

                elif den == -1:
                    return sformal(f'{-num}·³√{rdc}')

                elif den > 0:
                    return sformal(f'{num}·³√{rdc}/{den}')

                elif den < 0:
                    return sformal(f'{-num}·³√{rdc}/{-den}')

            # ³√(rtn ± cef√rdc) / den
            else:
                rdc = square(radicand)[1]
                fct = math.gcd(rational, square(radicand)[0])
                rtn = rational * cube(fct)[1] // fct
                cef = square(radicand)[0] * cube(fct)[1] // fct
                gcd = math.gcd(cube(fct)[0], denominator)
                num = cube(fct)[0] // gcd
                den = denominator // gcd

                if den == 1:
                    if is_minus:
                        return cformal(f'{num}·³√({rtn}-{cef}√{rdc})')

                    else:
                        return cformal(f'{num}·³√({rtn}+{cef}√{rdc})')

                elif den == -1:
                    if is_minus:
                        return cformal(f'{-num}·³√({rtn}-{cef}√{rdc})')

                    else:
                        return cformal(f'{-num}·³√({rtn}+{cef}√{rdc})')

                elif den > 0:
                    if is_minus:
                        return cformal(f'{num}·³√({rtn}-{cef}√{rdc})/{den}')

                    else:
                        return cformal(f'{num}·³√({rtn}+{cef}√{rdc})/{den}')

                elif den < 0:
                    if is_minus:
                        return cformal(f'{-num}·³√({-rtn}-{cef}√{rdc})/{-den}')

                    else:
                        return cformal(f'{-num}·³√({-rtn}+{cef}√{rdc})/{-den}')

        # fraction is a complex number
        elif radicand < 0:
            # ³√(rtn ± cef√rdc*i) / den
            rdc = square(-radicand)[1]
            fct = math.gcd(rational, square(-radicand)[0])
            rtn = rational * cube(fct)[1] // fct
            cef = square(-radicand)[0] * cube(fct)[1] // fct
            gcd = math.gcd(cube(fct)[0], denominator)
            num = cube(fct)[0] // gcd
            den = denominator // gcd

            if den == 1:
                if is_minus:
                    return cformal(f'{num}·³√({rtn}-{cef}√{rdc}i)')

                else:
                    return cformal(f'{num}·³√({rtn}+{cef}√{rdc}i)')

            elif den == -1:
                if is_minus:
                    return cformal(f'{-num}·³√({rtn}-{cef}√{rdc}i)')

                else:
                    return cformal(f'{-num}·³√({rtn}+{cef}√{rdc}i)')

            elif den > 0:
                if is_minus:
                    return cformal(f'{num}·³√({rtn}-{cef}√{rdc}i)/{den}')

                else:
                    return cformal(f'{num}·³√({rtn}+{cef}√{rdc}i)/{den}')

            elif den < 0:
                if is_minus:
                    return cformal(f'{-num}·³√({-rtn}-{cef}√{rdc}i)/{-den}')

                else:
                    return cformal(f'{-num}·³√({-rtn}+{cef}√{rdc}i)/{-den}')

        # ³√rational / denominator
        else:
            rdc = cube(rational)[1]
            gcd = math.gcd(cube(rational)[0], denominator)
            num = cube(rational)[0] // gcd
            den = denominator // gcd

            if den == 1:
                return sformal(f'{num}·³√{rdc}')

            elif den == -1:
                return sformal(f'{-num}·³√{rdc}')

            elif den > 0:
                return sformal(f'{num}·³√{rdc}/{den}')

            elif den < 0:
                return sformal(f'{-num}·³√{rdc}/{-den}')

# simplify cubic roots
def cubic_root(rational: int, radicand: int=0, denominator: int=1, is_minus: bool=False) -> str:
    """
    automatically simplify and format cubic roots

    parameters:
        rational: the integer in numerator of the cubic root
        radicand: the radicand in numerator of the cubic root (default as 0)
        denominator: the denominator of the cubic root (default as 1)
        is_minus: change the '+' between rational and radicand into '-' (default as False)

    return:
        formatted string of the mathematical expression

    examples:
        >>>cubic_root(5, 3, 8, True)
        '³√(5-√3)/8'
        >>>cubic_root(12)
        '³√12'
        >>>cubic_root(0, -5)
        '-⁶√5i'
        >>>cubic_root(-32, -704)
        '1-√11i'
        >>>cubic_root(-48, -64, 3, True)
        '2·³√(-6-i)/3'
        >>>cubic_root(-64800, 33139243584)
        '-6+6√33·³√3'
    """
    # ± ⁶√radicand / denominator
    if rational == 0:
        if is_minus:
            return cbfrac(0, radicand, denominator, True)

        else:
            return cbfrac(0, radicand, denominator)

    # ³√(rational ± √radicand) / denominator
    else:
        # case for real number
        if radicand > 0:
            fct = math.gcd(rational, square(radicand)[0])
            rtn = rational // fct
            rdc = radicand // fct ** 2
            R1 = (rtn ** 2 - rdc) * (rtn + math.sqrt(rdc))
            R2 = (rtn ** 2 - rdc) * (rtn - math.sqrt(rdc))
            x = round(rtn/4+3*(cbrt(R1)+cbrt(R2))/8)

            if is_cube(x):
                pass

            else:
                x = 0

            R1 = (rational ** 2 - radicand) * (rational + math.sqrt(radicand))
            R2 = (rational ** 2 - radicand) * (rational - math.sqrt(radicand))
            y = round(rational/4+3*(cbrt(R1)+cbrt(R2))/8)

            if is_cube(y):
                pass

            else:
                y = 0

            if x != 0 and is_cube((rtn-x)**3//(27*x)):
                a = cube(fct)[0] * cube(x)[0]
                b = cube(fct)[0] ** 2 * (rtn - x) // (3 * cube(x)[0])

                if is_cube(fct):
                    if is_minus:
                        return sqfrac(a, b, denominator, True)

                    else:
                        return sqfrac(a, b, denominator)

                else:
                    if is_minus:
                        return f'{sqfrac(a, b, denominator, True)}·{cubic_root(cube(fct)[1])}'

                    else:
                        return f'{sqfrac(a, b, denominator)}·{cubic_root(cube(fct)[1])}'

            elif y != 0 and is_cube((rational-y)**3//(27*y)):
                a = cube(y)[0]
                b = (rational - y) // (3 * cube(y)[0])

                if is_minus:
                    return sqfrac(a, b, denominator, True)

                else:
                    return sqfrac(a, b, denominator)

            else:
                if is_minus:
                    return cbfrac(rational, radicand, denominator, True)

                else:
                    return cbfrac(rational, radicand, denominator)

        # case for complex number
        elif radicand < 0:
            fct = math.gcd(rational, square(-radicand)[0])
            rtn = rational // fct
            rdc = radicand // fct ** 2
            theta = math.atan(math.sqrt(-rdc)/abs(rtn))
            z1 = round(abs(rtn)/4+3*math.sqrt(rtn**2-rdc)*math.cos(theta/3)/4)
            z2 = round(abs(rtn)/4+3*math.sqrt(rtn**2-rdc)*math.cos(theta/3+2*math.pi/3)/4)
            z3 = round(abs(rtn)/4+3*math.sqrt(rtn**2-rdc)*math.cos(theta/3+4*math.pi/3)/4)

            if is_cube(z1):
                x = z1

            elif is_cube(z2):
                x = z2

            elif is_cube(z3):
                x = z3

            else:
                x = 0

            theta = math.atan(math.sqrt(-radicand)/abs(rational))
            z1 = round(abs(rational)/4+3*math.sqrt(rational**2-radicand)*math.cos(theta/3)/4)
            z2 = round(abs(rational)/4+3*math.sqrt(rational**2-radicand)*math.cos(theta/3+2*math.pi/3)/4)
            z3 = round(abs(rational)/4+3*math.sqrt(rational**2-radicand)*math.cos(theta/3+4*math.pi/3)/4)

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

            if x != 0 and is_cube((rtn-x)**3//(27*x)):
                a = cube(fct)[0] * cube(x)[0]
                b = cube(fct)[0] ** 2 * (rtn - x) // (3 * cube(x)[0])

                if is_cube(fct):
                    if is_minus and 3 * a ** 2 + b > 0 or not is_minus and 3 * a ** 2 + b < 0:
                        return sqfrac(a, b, denominator, True)

                    else:
                        return sqfrac(a, b, denominator)

                else:
                    if is_minus and 3 * a ** 2 + b > 0 or not is_minus and 3 * a ** 2 + b < 0:
                        return f'{sqfrac(a, b, denominator, True)}·{cubic_root(cube(fct)[1])}'

                    else:
                        return f'{sqfrac(a, b, denominator)}·{cubic_root(cube(fct)[1])}'

            elif y != 0 and is_cube((rational-y)**3//(27*y)):
                a = cube(y)[0]
                b = (rational - y) // (3 * cube(y)[0])

                if is_minus and 3 * a ** 2 + b > 0 or not is_minus and 3 * a ** 2 + b < 0:
                    return sqfrac(a, b, denominator, True)

                else:
                    return sqfrac(a, b, denominator)

            else:
                if is_minus:
                    return cbfrac(rational, radicand, denominator, True)

                else:
                    return cbfrac(rational, radicand, denominator)

        # case for radicand = 0
        else:
            return cbfrac(rational, 0, denominator)
