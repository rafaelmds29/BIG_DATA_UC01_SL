#Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente.
qtd_par = 0
qtd_impar = 0
num = [1,8,3,4,5,7,21,11,2,10]
for i in range(len(num)):
    if num[i] % 2 == 0:
        qtd_par += 1
    else:
        qtd_impar += 1
print(f'A quantidade de números pares é: {qtd_par}')
print(f'A quantidade de números impares é: {qtd_impar}')
print('Ordem de criação')
print(num)
print('Ordem inversa')
num.reverse()
print(f'A ordem inversa da lista é: {num}')
print('Ordem crescente')
num.sort()
print(f'A ordem crescente da lista é: {num}')