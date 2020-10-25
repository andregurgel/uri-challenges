from math import sqrt

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (a > 0) & (b > 0) & (c > 0):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('Impossivel calcular')
    elif delta == 0:
        x1 = (-1 * b) / (2 * a)
        print('R1 = {0:.4f}'.format(x1))
        x2 = (-1 * b) / (2 * a)
        print('R2 = {0:.4f}'.format(x2))
    else:
        x1 = ((b * (-1)) + sqrt(delta)) / (2 * a)
        x2 = ((b * (-1)) - sqrt(delta)) / (2 * a)
        print('R1 = {0:.5f}'.format(x1))
        print('R2 = {0:.5f}'.format(x2))
else:
    print('Impossivel calcular')