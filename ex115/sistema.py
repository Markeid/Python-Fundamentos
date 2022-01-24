from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar um nova pessoa
        cabeçalho('Novo Cadastro')
        n = str(input('Nome: '))
        i = leiaInt('Idade: ')
        cadastrar(arq, n, i)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até mais!')
        break
    else:
        print('\033[mERRO! Digite uma opção válida!\033[m')
    sleep(2)
