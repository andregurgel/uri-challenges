n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

def calcularMedia(nota1, nota2, nota3, nota4):
    return ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / (10)

def calcularMediaFinal(media, nota5):
    return (media + nota5) / 2

media = calcularMedia(n1, n2, n3, n4)
print('Media: {0:.1f}'.format(media))

if media < 5.0:
    print('Aluno reprovado.')
elif (media >= 5.0) & (media <= 6.9):
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: {0:.1f}'.format(n5))
    mediaFinal = calcularMediaFinal(media, n5)
    if mediaFinal >= 5:
        print('Aluno aprovado.')
        print('Media final: {0:.1f}'.format(mediaFinal))
    else:
        print('Aluno reprovado.')
        print('Media final: {0:.1f}'.format(mediaFinal))

else:
    print('Aluno aprovado.')