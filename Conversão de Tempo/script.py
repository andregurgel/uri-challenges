time = int(input())
conversion = [0,0,0]

if time >= 3600:
    conversion[0] = time // 3600
    time = time % 3600
    if time != 0:
        conversion[1] = time // 60
        time = time % 60
        if time != 0:
            print(time)
            conversion[2] = time
elif time >= 60 & time < 3600:
    conversion[1] = time // 60
    if time % 60 != 0:
        conversion[2] = time % 60
else:
    conversion[2] = time

print('{}:{}:{}'.format(conversion[0], conversion[1], conversion[2]))