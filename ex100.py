from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {lista}, temos {s}')

números = list()
sorteia(números)
somaPar(números)
