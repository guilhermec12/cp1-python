x = float(input('input X value'))
y = float(input('input Y value:'))


if x == 0 and y == 0:
    print('the point is at the origin')


elif x == 0:
    print('the point is on the axis Y')

elif y == 0:
    print('the point is on the axis X')


elif x > 0 and y > 0:
    print('quadrant 1')

elif x < 0 and y > 0:
    print('quadrant 2')

elif x < 0 and y < 0:
    print('quadrant 3')

elif x > 0 and y < 0:
    print('quadrant 4')