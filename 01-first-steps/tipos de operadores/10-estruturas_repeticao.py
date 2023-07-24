texto = input("informe um texto\n")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# For else

texto = input("informe um texto\n")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print('Executa fora do laço')
print()