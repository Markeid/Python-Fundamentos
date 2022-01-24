t = list()
j = dict()
p = list()

while True:
    j.clear()
    j['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {j["Nome"]} jogou? '))
    p.clear()
    for x in range(0, tot):
        p.append(int(input(f'   Quantos gols na partida {x+1}? ')))
    j['Gols'] = p[:]
    j['Total'] = sum(p)
    t.append(j.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if r == 'N':
        break

print('-=' * 30)
print('cod ', end=' ')
for y in j.keys():
    print(f'{y:<15}', end=' ')
print()
print('-' * 40)

for a, b in enumerate(t):
    print(f'{a:>3} ', end=' ')
    for c in b.values():
        print(f'{str(c):<15}', end=' ')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (Digite 999 para encerrar) '))
    if busca == 999:
        break
    if busca >= len(t):
        print(f'Erro! Não existe com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {t[busca]["Nome"]}:')
        for d, e in enumerate(t[busca]["Gols"]):
            print(f'     No jogo {d+1} fez {e} gols.')
print('-' * 40)
print('<<FIM!>>')
