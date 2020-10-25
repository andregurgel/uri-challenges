codigo, quantidade = input().split()

codigo = int(codigo)
quantidade = int(quantidade)

cardapio = [[1, 'Cachorro Quente', 4.0], [2, 'X-Salada', 4.50], [3, 'X-Bacon', 5.0], [4, 'Torrada Simples', 2.0], [5, 'Refrigerante', 1.5]]

precoFinal = cardapio[codigo-1][2] * quantidade

print('Total: R$ {0:.2f}'.format(precoFinal))