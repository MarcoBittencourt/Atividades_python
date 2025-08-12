#8 questão
texto = input('coloque a palavra parra identificação de índice: ').strip()
caractere = input('coloque o caractere que deseja achar o indice: ').strip()
indice = texto.find(caractere)
print('local do indice: ',indice)