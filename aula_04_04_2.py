#Praticando 2 e 3
soma = 0
maior = 0
num_maior = 0
nome_maior = ""
for i in range(3):
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe a sua idade: '))
    if idade > maior:
        maior = idade
        num_maior = nome
    soma = soma + idade
    media = soma / (i + 1)
print(f'A soma das idades é {soma}, enquanto a média é {media:.2f}')
print(f"A pessoa mais velha é {num_maior}")