def voto(ano):
    from datetime import date
    a = date.today().year
    i = a - ano
    if i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    elif 16 <= i < 18 or i > 65:
        return f'Com {i} anos: VOTO OPCIONAL.'
    else:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'

#Programa Principal
n = int(input('Ano de nascimento: '))
print(voto(n))
