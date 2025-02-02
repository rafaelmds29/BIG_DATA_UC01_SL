nome = input('Informe o nome: ')
while True:
    sexo = input('Informe o sexo (M ou F): ')
    if sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f':
        break
    else:
        print('Informe "M" ou "F" para o sexo')
while True:
    try:
        idade = int(input('Informe a idade: '))
    except ValueError:
        print('Verifique a idade digitada')
    else:
        if sexo == 'M' or sexo == 'm':
            print(f'Seja bem vindo, senhor {nome}')
        else:
            print(f'Seja bem vindo, senhora {nome}')
        break