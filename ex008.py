medida = float(input('Distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('a distância {}m, em cm é igual a {:.0f}cm e em mm é igual a {:.0f}mm'.format(medida, cm, mm))