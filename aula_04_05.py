#Praticando 4
for i in range(3):
    nome = input('Informe o seu nome: ')
    nota_1 = float(input('Informe a sua primeira nota: '))
    nota_2 = float(input('Informe a sua segunda nota: '))
    media = (nota_1 + nota_2) / (i + 1)
    if media >= 70:
        print(f'Sr(a) {nome}, a sua média é {media}: ATENDIDO')
    elif media >= 30 and media < 70:
        print(f'Sr(a) {nome}, a sua média é {media}: PARCIALMENTE ATENDIDO')
    else:
        print(f'Sr(a) {nome}, a sua média é {media}: NÃO ATENDIDO')