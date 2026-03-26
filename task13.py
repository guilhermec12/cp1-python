import math

A = float(input('digite o valor de A: '))
B = float(input('digite o valor de B: '))
C = float(input('digite o valor de C: '))

if A == 0:
    print('nao e uma equacao do segundo grau.')
else:
    delta = B ** 2 - 4 * A * C
    print('delta =', delta)

    if delta < 0:
        print('nao ha raizes reais')

    elif delta == 0:
        x = -B / (2 * A)
        print('raiz unica:', x)

    else:
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)
        print('duas raizes reais:')
        print('x1 =', x1)
        print('x2 =', x2)