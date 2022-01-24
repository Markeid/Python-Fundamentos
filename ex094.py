g = list()
p = dict()
s = m = 0

while True:
    p.clear()
    p['Nome'] = str(input('Nome: '))
    while True:
        p['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if p['Sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    p['Idade'] = int(input('Idade: '))
    s += p['Idade']
    g.append(p.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if r == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(g)} pessoas cadastradas.')
m = s / len(g)
print(f'B) A média de idade é de {m:5.2f} anos.')
print(f'C) As mulheres cadastras foram ', end=' ')
for x in g:
    if x['Sexo'] in 'Ff':
        print(f'{x["Nome"]} ', end=' ')
print()
print(f'D) Lista das pessoas que estão acima de média: ')
for x in g:
    if x['Idade'] >= m:
        print('      ', end=' ')
        for a, b in x.items():
            print(f'{a} = {b}; ', end=' ')
        print()
print('<<ENCERRADO>>')
