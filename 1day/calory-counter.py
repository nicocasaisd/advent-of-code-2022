'''
--- Day 1: Calorie Counting ---
'''

'''
 Part 1
'''

'''
#file = open('input-min', 'r') # input de prueba
file = open('input', 'r')

acumulador = 0
max_calories = 0

print("Using loop")
for line in file:
    try:
        entero = int(line.strip())
        acumulador += entero
    except ValueError:
        pass
        
    if(line == '\n'):
        if(acumulador > max_calories):
            max_calories = acumulador
        acumulador = 0


print(f"Valor maximo : {max_calories}")

'''

'''
 Part 2
'''

#file = open('input-min', 'r') # input de prueba
file = open('input', 'r')

acumulador = 0
lista_calorias = []

print("Using loop")
for line in file:
    try:
        entero = int(line.strip())
        acumulador += entero
    except ValueError:
        pass
        
    if(line == '\n'):
        lista_calorias.append(acumulador)
        acumulador = 0

lista_calorias.sort(reverse=True)
suma_calorias = 0

for i in range(3):
    suma_calorias += lista_calorias[i]

print(f"Suma de las calorias de los primeros 3: {suma_calorias}")