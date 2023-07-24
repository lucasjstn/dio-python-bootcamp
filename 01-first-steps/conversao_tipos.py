preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = int(preco)
print(preco)

# Fazer divisão de um número inteiro usando duas barras retorna o valor em numero inteiro
print(3 // 2)

print(f'------------------------')

preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f'idade {idade} preco {preco}'
print(texto)

print(f'------------------------')

preco = '10.50'
idade = 28

print(float(preco))
print(type(float(preco)))
print(int(idade))
try:
    print(float('python'))
except ValueError as error:
    print(error)
