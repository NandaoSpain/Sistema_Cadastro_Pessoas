from SistemaCadastro.lib.Interface import *
from SistemaCadastro.lib.arquivo import *
from time import sleep

arq = 'CursoemVideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resp = menu(['Listar Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo('CursoemVideo.txt')
    elif resp == 2:
        cabeçalho('CADASTRO DE PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do Programa... Até logo!')
        break
    else:
        print(f'\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
