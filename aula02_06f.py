#Programa velocidade média e consumo
distancia = float(input('Insira a distância percorrida (metros):'))
tempo = float(input('Insira o tempo percorrido: '))
velocidade_media = distancia / tempo
consumo = distancia / 12
print(f'A velocidade média de sua viagem foi {velocidade_media:.2f} km/h, enquanto o consumo médio foi de {consumo} km/l')