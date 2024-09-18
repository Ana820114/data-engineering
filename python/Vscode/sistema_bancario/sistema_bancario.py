# sistema bancario

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
nu_saques = 0
LIMITE_SAQUES = 3

while True:
        opcao = input(menu)
        
        if opcao == "d":
            print("Depositar")
        
        elif opcao == "s":
            print("Sacar")
        
        elif opcao == "e":
            input("Extrato")
        
        elif opcao == "q":
            print("Sair")
            break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")