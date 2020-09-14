vendedor = input()
salario = float(input())
vendas = float(input())

salarioFinal = salario + ((vendas) * (15/100))
print('TOTAL = R$ {0:.2f}'.format(salarioFinal))