codigoP1, numeroP1, valorP1 = input().split()
codigoP2, numeroP2, valorP2 = input().split()

codigoP1 = int(codigoP1)
numeroP1 = int(numeroP1)
valorP1 = float(valorP1)

codigoP2 = int(codigoP2)
numeroP2 = int(numeroP2)
valorP2 = float(valorP2)

total = ((numeroP1 * valorP1) + (numeroP2 * valorP2))
print('VALOR A PAGAR: R$ {0:.2f}'.format(total))