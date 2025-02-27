"""
Programa: ex14_pontos
Descrição: Este programa calcula a distância entre dois pontos.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""

# Alocação de memória 
import math

# Entrada de dados 

x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))
x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))

# Processamento de dados 

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Saída de dados 

print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {distancia:.2f}")