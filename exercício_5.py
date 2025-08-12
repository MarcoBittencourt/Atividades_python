#5 questão
n = int(input("Fale a quatidade total de notas: "))
notas = []
for _ in range(n):
    nota = float(input("digite as notas: "))
    notas.append(nota)
media = sum(notas) / n
limite_superior = media * 1.10
limite_inferior = media * 0.90
acima_10 = 0
abaixo_10 = 0
for nota in notas:
    if nota > limite_superior:
        acima_10 += 1
    elif nota < limite_inferior:
        abaixo_10 += 1
print(f"Média: {media:.2f}")
print("n° de notas 10% acima da média:", acima_10)
print("n° de notas 10% 1abaixo da média:", abaixo_10)