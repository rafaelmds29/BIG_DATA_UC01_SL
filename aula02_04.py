#Programa Calcular Idade
import datetime #Importa a biblioteca datetime
nascimento = int(input('Insira o seu ano de nascimento: '))
data_atual = datetime.date.today() #Armazena a data completa
ano_atual = data_atual.year #Armazena na variável ano_atual
idade = ano_atual - nascimento
print(f'Você tem {idade} anos.')