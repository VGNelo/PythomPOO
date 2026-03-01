'''
import speedtest

test = speedtest.Speedtest()

down_speed = test.download()
up_speed = test.upload()

print('Download speed', down_speed)
print('Upload', up_speed)

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

# Exibe o resumo dos alunos e médias
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# Mostra notas detalhadas de alunos selecionados pelo índice
while True:
    print('-' * 35)
    opc = input('Mostrar notas de qual aluno? (999 interrompe): ')

    # Verifica se o usuário digitou "999" para finalizar
    if opc == "999":
        print('FINALIZANDO...')
        break  # Sai do loop

    # Verifica se o valor digitado é um número e está dentro do intervalo de índices válidos
    if opc.isdigit():  # Verifica se a entrada é um número
        opc = int(opc)  # Converte a entrada de texto para inteiro
        if 0 <= opc < len(ficha):  # Verifica se o índice é válido
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        else:
            print('Aluno não encontrado. Digite um número válido.')
    else:
        # Caso o input não seja válido (ex.: letras ou caracteres inválidos)
        print('Entrada inválida. Por favor, digite um número correspondente.')

pessoas = {'nome': 'Zé', 'idade': 23, 'sexo': 'M'}
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas['sexo'])
print(pessoas.items())
del pessoas['sexo']
pessoas['cidade'] = 'Pinda'
pessoas['nome'] = 'Zeze'
for K, i in pessoas.items():
    print(f'{K} = {i}')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
#print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'o campos {k} tem valor {v}')

nun = str(input('Digite seu nome: ')).lower()
if 'João' in nun:
    print(f'O nome {nun} está na frase')
else:
    print(f'O nome {nun} não está na frase')

aluno = dict()
aluno ['nome'] = str(input('Nome: ')).upper()
aluno ['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno ['média'] >= 7:
    aluno ['situação'] = 'Aprovado'
elif 5 <= aluno ['média'] < 7:
    aluno ['situação'] = 'Recuperação'
else:
    aluno ['situação'] = 'Reprovado'
print('-=' * 30)
for k,v in aluno.items():
    print(f'  -   {k} é igual a {v}')

from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador 1': randint(1, 6),
         'jogador 2': randint(1, 6),
         'jogador 3': randint(1, 6),
         'jogador 4': randint(1, 6),}
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'O {k} tioru o valor {v} no dado' )
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)


from datetime import datetime
dados = dict()
dados ['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados ['idade'] = datetime.now().year - nasc
dados ['CTPS'] = int(input('Numero da CTPS (0 se não tem): '))
if dados ['CTPS'] != 0:
    dados ['contratação'] = int(input('Ano de contratação: '))
    dados ['sálario'] = float(input('Salario: R$ '))
    dados ['aposentado

jogador = dict()
partidas = list()
jogador ['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogo: '))
for c in range(total):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = partidas [:]
jogador["tot"] = sum(partidas)
print('-+' * 30)
print(jogador)
print('-+' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas') #pode {len(jogador["gols"]}
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["tot"]} gols')
from math import gamma



galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite um nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break  # Isso interrompe o loop principal

print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};     ', end='')
        print()
print('<<Encerrado>>')

def ilustração():
    print('-' * 30)
    print()

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('Essa é a mensagem')
ilustração()

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} e {b} é igual a {s}')


soma(4, 2)
ilustração()

def contador(* num):
    print(num)


contador(1, 2, 3)
contador(4, 5, 6)
contador(8, 9, 0)
ilustração()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)
ilustração()

#função
def soma(a, b):
    s = a + b
    print(s)


#programa principal
soma(2, 4)
soma(2, 3)
soma(1, 2)

def área(l, c):
    a = l * c
    print(f'A área de um terreno de {l} * {c} é de {a}m²')

#programa principal
print('        Controle de terreno        ')
print('-' * 45)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m) '))
área(l, c)



def escrever(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escrever('olá')
escrever("Mundo!")
escrever('Olá Mundo!')




def func(x):
    return x * 2

y = 7
print(func(y))

from time import sleep

def maior(*núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior == valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 4, 7, 5 ,8 ,9, 3)
maior(7, 8, 1)


from  random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos  {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros) ''

def sacar_dinheiro(valor):
    notas =  [100, 50, 20, 10, 5, 2, 1]
    print(f'\nSaando R$ {valor:.2f} em cédulas: ')
    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            print(f'{quantidade} de nota(a)) cédulas de R$ {nota:.2f}')
            valor -= quantidade * nota
valor_saque = int(input('Digite o valor que deseja sacar: R$ '))
sacar_dinheiro(valor_saque)
print('Operação concluída com sucesso!')

def voto(ano):
    from datetime import date  # Importação local

    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional.'
    else:
        return f'Com {idade} anos: Voto obrigatório.'

# Programa principal
nasc = int(input("Que ano você nasceu? "))
print(voto(nasc))


def fatorial(n, show=False):
    """
    -> calcula o fatorial de um numero.
    :param o n: O numero a ser calculado.
    :param o show: (opcional) mostrar ou não a conta.
    :return: O valor fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            f *= c
    return f


# Programa princiapl
print(fatorial(5, show=True))
help(fatorial)

def ficha(jogo = '<desconhecido>', gol = 0):
    print(f'O jogador {jogo} fez {gol} gol(s) no campeonato')


#programa principal
n = str(input("Nome do jogador: "))
g = str(input("Números de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')

# Exemplo de uso
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')

def ajuda(com):
    help(com)


#programa principal
comando =''
while True:
    comando = str(input("Função ou Biblioteca > ")).strip()
    if comando.upper == 'Fim':
        break
    else:
        ajuda(comando)

def notas(*n, sit=False):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n) / len(n)
    if sit:
        if r["média"] >= 7:
            r["situação"] = "Boa"
        elif r["média"] >= 5:
            r["situação"] = "Razoável"
        else:
            r["situação"] = "Ruim"
    return r

resp = notas(10,5.5, 2.5, 9, 8.5, sit=True)
print(resp)


from colorama import init, Fore, Back, Style
init(autoreset=True)

def ajuda(comando):
    print(Fore.YELLOW + Style.BRIGHT + f"Acessando o manual do comando '{comando}'...\n")
    print(Fore.GREEN + Style.NORMAL)
    help(comando)

def titulo(msg, cor=Fore.CYAN):
    print(cor + Style.BRIGHT + "-" * 40)
    print(cor + Style.BRIGHT + f"{msg.center(40)}")
    print(cor + Style.BRIGHT + "-" * 40)

while True:
    titulo("SISTEMA DE AJUDA PYTHON", Fore.MAGENTA)
    comando = input(Fore.WHITE + Style.BRIGHT + "Digite um comando ou 'FIM' para sair: ").strip()
    if comando.upper() == 'FIM':
        titulo("ENCERRANDO...", Fore.RED)
        break
    else:
        ajuda(comando)

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")

a = 12543765.885
print(f'o valor de {a:,.2f}')

x = [1, 2, 3]
x.insert(3, 99)
print(x)

def LeiaError(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mError: Por favor digite um número inteiro válido\033[m')
            continue
        else:
            return n

nun = LeiaError('Digite um valor: ')
print(f'O valor digitado foi {nun}')

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/VGNelo/Alura-Analise-de-dados1---lojas-alura')
except urllib.error.URLError:
    print('O site não esta funcionando normalmente')
else:
    print('O site esta funcionando normalmente')'''








