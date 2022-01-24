from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2.5)

    if a < b:
        cont = 1
        while cont <= b:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont -= c
        print('FIM!')

#Programa Principal

contador(1,10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Personalize a contagem: ')
x = int(input('Ínicio: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x, y, z)

