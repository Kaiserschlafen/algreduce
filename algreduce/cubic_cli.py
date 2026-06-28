from cubic_solver import solve_cubic

def main():
    print('Hi! I can help you solve cubic equation: ax³ + bx² + cx + d = 0!')

    try:
        a = int(input('Please enter the value a: '))
        b = int(input('Please enter the value b: '))
        c = int(input('Please enter the value c: '))
        d = int(input('Please enter the value d: '))

        result = solve_cubic(a, b, c, d)

        if result['number of roots'] == 1:
            print(f'The equation has 1 root: x = {result['roots'][0]}')

        elif result['number of roots'] == 2:
            print(f'The equation has 2 roots: x₁ = {result['roots'][0]} and x₂ = {result['roots'][1]}')

        elif result['number of roots'] == 3:
            print(f'The equation has 3 roots: x₁ = {result['roots'][0]} and x₂ = {result['roots'][1]} and x₃ = {result['roots'][2]}')

        input('\nThe program has finished execution, press any key to exit.\n')

    except ZeroDivisionError:
        print('Value \'a\' can\'t be 0!')

        input('\nPlease try again, press any key to exit.\n')

    except ValueError:
        print('I\'m sorry! a, b, c, d are supposed to be integers!')

        input('\nPlease try again, press any key to exit.\n')

if __name__ == '__main__':
    main()
