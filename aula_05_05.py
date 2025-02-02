
gabarito = ['A', 'B', 'B', 'D', 'E']
resposta = []
qtd_acerto = 0
qtd_erro = 0
for i in range(len(gabarito)):
    resposta.append(input('Informe a resposta: '))
    if gabarito[i] == resposta[i]:
        qtd_acerto += 1
    else:
        qtd_erro += 1
print(f'As suas respostas foram: {resposta}. Você acertou {qtd_acerto} e errou {qtd_erro}')