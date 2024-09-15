nome = "gUilhErmE"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá Mundo   "

print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

# interpolação de variaveis

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# metodo format.

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao,
linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade,nome))

# f-string

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# fatiamento 

nome = "Guilherme Arthur de Carvalho"

nome[0]

nome[:9]

nome[10:]

nome[10:16]

nome[10:16:2]

nome[:]

nome[ :: -1]
