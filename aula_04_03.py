#Programa que realiza a soma dentre 5 números inteiros e fornece o maior valor
soma = 0
maior = 0
for i in range(5):
    num = int(input('Informe o valor: '))
    if num > maior:
        maior = num
    soma = soma + num #Acumulador
print(f'O resultado da soma é: {soma}, e o maior número informado é: {maior}')