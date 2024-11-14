#Programa Prestação em Atraso
prestacao = float(input('Insira o valor da prestação: '))
taxa = float(input('Insira a taxa mensal: '))
tempo = float(input('Insira a quantidade de meses em atraso: '))
valor_final = prestacao + (prestacao * (taxa/100) * tempo)
print(f'O valor final da sua prestação é R$ {valor_final:.2f}')