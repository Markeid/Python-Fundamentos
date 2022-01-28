l = float(input('Largura da Parede: '))
a = float(input('Altura da Parede: '))
ar = l * a
print('A dimensão da parede é de {}X{} e sua área é igual a {}m²'.format(l, a, ar))
t = ar / 2
print('Para pintar a parede precisará de {:.0f}l de tinta'.format(t))