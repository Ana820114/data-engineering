#um desvio
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
    
if saldo < saque:
    print("Saldo insuficiente!")
    
# dois desvios de controle if/else
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else: 
    print("Saldo insuficiente!")
    
# três devios de controle if/elif/else

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informa sua idade:"))

if idade >= MAIOR_IDADE:
    print("MAior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
        print("Pode fazer aulas teóricas, mas não pode fazer aulas praticas.")
else:
    print("Ainda não pode tirar CNH.")
    

