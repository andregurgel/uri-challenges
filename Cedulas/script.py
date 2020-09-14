value = int(input())
print(value)

def divider(value, div):
    if value >= div:
        notes = value // div
        return notes
    else:
        return 0

def recursive(value, array, cont, slotsNotes):
    while value > 0:
        n = divider(value, array[cont])
        slotsNotes[cont] = n
        value -= (array[cont] * n)
        cont += 1
        recursive(value, array, cont, slotsNotes)

def printer(array, slotsNotes):
    for i in range(len(array)):
        print('{} nota(s) de R$ {},00'.format(slotsNotes[i], array[i]))

array = [200, 100, 50, 20, 10, 5, 2, 1]
slotsNotes = [0, 0, 0, 0, 0, 0, 0, 0]
cont = 0
recursive(value, array, cont, slotsNotes)
printer(array, slotsNotes)