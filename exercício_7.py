#7 questão
def obter_caractere_entrada(prompt):
    while True:
        caractere = input(prompt).strip()
        if len(caractere) == 1:
            return caractere
        else:
            print("Por favor, insira apenas um caractere.")
texto = input('Coloque a palavra ou frase: ').strip()
caractere_antigo = obter_caractere_entrada('Coloque o caractere que deseja trocar: ')
caractere_novo = obter_caractere_entrada('Coloque o caractere pelo qual deseja trocar: ')
texto_modificado = texto.replace(caractere_antigo, caractere_novo)
print('Texto alterado: ', texto_modificado)