saldo = 100
saque = 200
limite = 100

saldo >= saque and saque <= limite 
saldo >= saque or saque <= limite 

# operador de negação

contatos_emergencia = []

not 100 > 150

# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

# parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)


