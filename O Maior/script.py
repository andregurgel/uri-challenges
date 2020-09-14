a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
    if a > c:
        print('{} eh o maior'.format(a))
    else:
        print('{} eh o maior'.format(c))
else:
    if b > c:
        print('{} eh o maior'.format(b))
    else:
        print('{} eh o maior'.format(c))