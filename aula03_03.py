#Programa com desvio e conectivo
nome = input('Informe seu nome: ')
sexo = input('Informe o seu sexo (M ou F): ')
idade = int(input('Informe a sua idade: '))
if (idade >= 18) and (sexo == 'M' or sexo == 'm'):
    certificado = int(input(f'Olá, Sr {nome}. Informe seu número de certificado de reservista: '))
elif idade >= 18:
    print(f'Olá, Sr(a) {nome}. Você possui {idade} e é maior de idade.')
else:
    print(f'Olá, Sr(a) {nome}. Você possui {idade} e é menor de idade.')