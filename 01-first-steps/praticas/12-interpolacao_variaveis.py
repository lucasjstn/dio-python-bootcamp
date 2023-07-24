nome = "lucas"
idade = 24
profissao = "rpa analyst"
linguagem = "blue prism"

print("Olá, me chamo %s. Tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {0}. Tenho {1} anos de idade, trabalho com {2} e estou matriculado no curso de {3}".format(nome, idade, profissao, linguagem))

print("{nome}".format(nome=nome))