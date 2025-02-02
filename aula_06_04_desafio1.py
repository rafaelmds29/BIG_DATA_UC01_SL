#Desafio 1
salario_h = float(input('Informe o seu salário por hora: '))
horas = int(input('Informe o número de horas trabalhadas no mês: '))
salario_bruto = salario_h * horas
irrf = salario_bruto * (11 / 100)
inss = salario_bruto * (8 / 100)
sindicato = salario_bruto * (5 / 100)
salario_liquido = salario_bruto - irrf - inss - sindicato
print(f'O salário bruto é R${salario_bruto:.2f}')
print(f'O valor pago de Imposto de Renda foi R${irrf:.2f}')
print(f'O valor pago ao INSS foi R${inss:.2f}')
print(f'O valor pago para o sindicato foi R${sindicato:.2f}')
print(f'O salário líquido é R${salario_liquido:.2f}')