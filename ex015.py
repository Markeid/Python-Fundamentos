d = int(input('Dias alugados: '))
km = float(input('Quantos Km rodados? '))
p = (d * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'. format(p))
