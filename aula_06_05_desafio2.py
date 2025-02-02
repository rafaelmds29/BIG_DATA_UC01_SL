#Desafio 2
temp = []
while True:
    temp.append(int(input('Informe a teperatura (°C): ')))
    continuar = input("Deseja adicionar outro habitante? (S/N): ")
    if continuar != 'S' and continuar != 's':
        break
print(f'A maior temperatura foi de {max(temp)}°C')
print(f'A menor temperatura foi de {min(temp)}°C')
print(f'A média das temperaturas foi de {sum(temp) / len(temp):.2f}°C')