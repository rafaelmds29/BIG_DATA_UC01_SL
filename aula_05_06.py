#Faça um programa que armazene em vetores o nome, a média e a situação de um grupo de 10 alunos. Ao final mostre o nome de cada aluno com sua respectiva situação.
nome = []
media = []
aprovado = 0
reprovado = 0
for i in range(2):
    nome.append(input('Informe seu nome: '))
    media.append(input('Informe sua média: '))
    num += 1
    if media[i] >= 70:
        print(f'Sr(a) {nome[i]}, você passou!')
    elif media[i] >= 30 and media[i] <70:
        print(f'Sr(a) {nome[i]}, você está de recuperação!')
    else:
        print(f'Sr(a) {nome}, você reprovou! ')