a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

numeros = [a, b, c]

crescente = sorted(numeros)

def printer(lista):
    for i in range(len(lista)):
        print(lista[i])

printer(crescente)
print('')
printer(numeros)