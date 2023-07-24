import sys
saldo = 500
quantidades_operacoes = 0
SAQUE_MAXIMO = 500 
LIMITE_OPERACOES = 3    
MENSAGEM_SEM_SALDO = f"""Você não possui saldo.
Encerrando operação..."""
operacoes = ""

menu = f"""
--------------------------------------

Bem vindo ao sistem bancário
Escolha uma opção:

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

---------------------------------------
"""

def sacar(valor, saldo, quantidades_operacoes):
    if valor > SAQUE_MAXIMO: 
        print(f'Operação não realizada.')
        print(f'O limite de saque diário é de R${SAQUE_MAXIMO:.2f}')
    elif saldo >= valor and quantidades_operacoes < LIMITE_OPERACOES: 
        saldo -= valor
        quantidades_operacoes += 1
        operacoes.join('Saque de R${valor}, Novo saldo: R${saldo}')
        print(f'Novo saldo: R${saldo:.2f}')
    else:
        print(f'Saldo insuficiente...')

def extrato():
    print(operacoes)

while True:
    valor = 0

    if saldo <= 0:
       print(MENSAGEM_SEM_SALDO)
       break

    print(menu)
    opcao = int(input())
    if opcao == 0:
        print('Obrigado.\nSeu saldo atual é de R${saldo:.2f}')
        sys.exit()
    elif opcao == 1:
        valor = int(input(f"Insira o valor do saque:\n"))
        sacar(valor, saldo, quantidades_operacoes)
    elif opcao == 2:    
        print()
    elif opcao == 3:
        extrato()