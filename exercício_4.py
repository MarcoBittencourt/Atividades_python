#4 questão
numero = int(input("Digite um número: "))
eh_primo = True
if numero <= 1:
    eh_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break
if eh_primo:
    print("Este número é Primo")
else:
    print("Este número não é Primo")