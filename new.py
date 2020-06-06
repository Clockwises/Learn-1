x = int(input('Some Integer : '))
for i in range(x+1)[::-1]:
    for j in range(i):
        print('*',end = '')
    print('')