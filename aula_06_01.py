#usuario fornece dois números inteiros e fazer o cálculo da divisão deles
while True:
    try:
        num_1 = int(input('Informe o número que você quer dividir: '))
        num_2 = int(input('Informe o divisor: '))
        divisao = num_1 / num_2
    except ZeroDivisionError:
        print('Verifique o segundo valor digitado, pois ele não pode ser 0')
    else:
        print(f'O resultado da divisão é: {divisao}')
        break