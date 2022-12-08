
print ('SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG')
c0de = int(input('Masukkan angka: '))

space = c0de-1
for afk in range(c0de):
    print (' '*space,end='')
    print('*' if  afk == 0 else '**' if afk  !=0 and afk !=c0de-1 else '*'*(c0de*2-1))
    space -=1
