#Programa Média com Desvio
nome = input('Informe seu nome: ')
nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <30:
    print(f'{nome}, sua média é {media}. Você está reprovado!')  
elif media >= 70:
    print(f'{nome}, sua média é {media}. Você está aprovado!')
else:
    print(f'{nome}, sua média é {media}. Você está de recuperação!')