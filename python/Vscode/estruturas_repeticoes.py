# for/ while

texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()# adiciona uma quebra de linha
    print("Executa no final do laço")
    
орсао = 1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando…")
    elif opcao == 2:
        print("Exibindo o extrato…")