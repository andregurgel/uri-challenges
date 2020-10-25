days = int(input())
conversion = [0,0,0]

if days >= 365:
    conversion[0] = days // 365
    days = days % 365
    if days != 0:
        conversion[1] = days // 30
        days = days % 30
        if days != 0:
            conversion[2] = days
elif days >= 30 & days < 365:
    conversion[1] = days // 30
    days = days % 30
    if days != 0:
        conversion[2] = days
else:
    conversion[2] = days

print('{} ano(s)'.format(conversion[0]))
print('{} mes(es)'.format(conversion[1]))
print('{} dia(s)'.format(conversion[2]))