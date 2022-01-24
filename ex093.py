j = dict()
p = list()
j['Nome'] = str(input('Nome do Jogador: '))
t = int(input(f'Quantas partidas {j["Nome"]} jogou? '))

for c in range(0, t):
    p.append(int(input(f'  Quantos gols na partida {c}? ')))
j['Gols'] = p[:]
j['Total'] = sum(p)
print('-=' * 30)
print(j)
print('-=' * 30)

for x, y in j.items():
    print(f'O campo {x} tem o valor {y}')
print('-=' * 30)
print(f'O jogador {j["Nome"]} jogou {len(j["Gols"])} partidas.')

for a, b in enumerate(j['Gols']):
    print(f'   => Na partida {a}, fez {b} gols.')
print(f'Foi um total de {j["Total"]} gols.')
