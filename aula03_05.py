idade = int(input('Informe a sua idade: '))
peso = float(input('Informa o seu peso (kg): '))
sono = int(input('Informe o quanto você dormiu nas últimas 24 horas: '))
if (idade >= 16) and (idade <= 69) and (peso > 50) and (sono >= 6):
    print('Você pode doar sangue.')
else:
    print('Você não pode doar sangue.')