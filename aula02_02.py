#Programa Peso Ideal
altura = float(input('Informe a sua altura (metros): '))
peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7
print(f'O peso ideal para a sua altura é {peso_ideal_homens:.2f}kg para homens e {peso_ideal_mulheres:.2f}kg para mulheres')