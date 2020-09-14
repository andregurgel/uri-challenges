a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159

def triangulo(base, altura):
    return (base * altura) / 2

def circulo(pi, raio):
    return (pi * (raio ** 2))

def trapezio(base1, base2, altura):
    return (altura * (base1+ base2)) / 2

def quadrado(lado):
    return lado ** 2

def retangulo(base, altura):
    return base * altura

print('TRIANGULO: {0:.3f}'.format(triangulo(a, c)))
print('CIRCULO: {0:.3f}'.format(circulo(pi, c)))
print('TRAPEZIO: {0:.3f}'.format(trapezio(a, b, c)))
print('QUADRADO: {0:.3f}'.format(quadrado(b)))
print('RETANGULO: {0:.3f}'.format(retangulo(a, b)))