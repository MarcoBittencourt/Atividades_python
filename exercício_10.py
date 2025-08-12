#10 questão
def main():
    n = int(input("Quantos números você deseja digitar? "))
    numeros = []
    for i in range(n):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)
    print("\na) Números na ordem inversa:")
    for num in reversed(numeros):
        print(num, end=' ')
    print("\n\nb) Números em ordem decrescente:")
    for num in sorted(numeros, reverse=True):
        print(num, end=' ')
if __name__ == "__main__":
    main()