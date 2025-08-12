#9 questão
x = int(input('insira o primeiro valor: '))
y = int(input('insira o segundo valor: '))
inicio = min(x, y)
fim = max(x, y)
for i in range(inicio + 1, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i, end=" ")