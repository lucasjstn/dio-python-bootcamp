saldo = 2000
saque = float(input("informe o valor do saque:"))

if saldo >= saque:
    print("realizando saque")

if saldo <= saque:
    print("saldo insuficiente")

print(f'!--------- usando elif -------2')

opcao = int(input("Informe uma opcao: \n[1] Sacar\n[2] Depositar"))

if opcao == 1:
    print(f'efetuando saque')
elif opcao == 2:
    printf(f'efetuando deposito')
else:
    sys.exit("opcao invalida")