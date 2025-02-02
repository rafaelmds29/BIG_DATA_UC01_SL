#Desafio 3
habitantes = []
while True:
    sexo = input("Informe o sexo (M/F): ")
    cor_olhos = input("Informe a cor dos olhos (azuis/verdes/castanhos): ")
    cor_cabelos = input("Informe a cor dos cabelos (louros/castanhos/pretos): ")
    idade = int(input("Informe a idade: "))
    habitantes.append((sexo, cor_olhos, cor_cabelos, idade))
    continuar = input("Deseja adicionar outro habitante? (S/N): ")
    if continuar != 'S' and continuar != 's':
        break
maior_idade = 0
qtd_f_18_35 = 0
qtd_verdes_louros = 0
for i in habitantes:
    sexo, cor_olhos, cor_cabelos, idade = i
    if idade > maior_idade:
        maior_idade = idade
    if (sexo == "F" or sexo == "f") and 18 <= idade <= 35:
        qtd_f_18_35 += 1
    if (cor_olhos == "verdes" or cor_olhos == "Verdes") and (cor_cabelos == "louros" or cor_cabelos == "Louros"):
        qtd_verdes_louros += 1
print(f"A maior idade dentre os habitantes é: {maior_idade}")
print(f"A quantidade de mulheres entre 18 e 35 anos é: {qtd_f_18_35}")
print(f"A quantidade de indivíduos com olhos verdes e cabelos louros é: {qtd_verdes_louros}")