'''
--- Day 2: Rock Paper Scissors ---
'''

'''
Part 1
'''

'''
def obtener_puntaje(input1, input2):
    puntaje = 0
    
    # Puntaje por forma elegida
    if input2 == 'X':
        puntaje += 1
    elif input2 == 'Y':
        puntaje += 2
    elif input2 == 'Z':
        puntaje += 3

    # Puntaje por resultado de partida
    if input2 == 'X':       #PIEDRA
        if input1 == 'A':
            puntaje += 3
        elif input1 == 'C':
            puntaje += 6
    elif input2 == 'Y':     #PAPEL
        if input1 == 'B':
            puntaje += 3
        elif input1 == 'A':
            puntaje += 6
    elif input2 == 'Z':     #TIJERA
        if input1 == 'C':
            puntaje += 3
        elif input1 == 'B':
            puntaje += 6
    
    return puntaje
        

puntaje_acumulado = 0

with open('input') as input:
    for line in input:
        puntaje_acumulado += obtener_puntaje(line[0], line[2])

print(f"Puntaje acumulado: {puntaje_acumulado}")

'''

'''
Solución encontrada online: https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-2-with-python/
'''
'''    
# Mapeamos los inputs con un diccionario

mapeo_input = {'A': 'Piedra', 'B': 'Papel', 'C': 'Tijera', 'X': 'Piedra', 'Y': 'Papel', 'Z': 'Tijera'}
puntaje_por_eleccion = {'Piedra' : 1, 'Papel': 2, 'Tijera': 3}
puntaje_por_resultado = {'Gano': 6, 'Empate': 3, 'Perdio': 0}

def obtener_puntaje_mapeo(input1, input2):
    rival_forma = mapeo_input[input1]
    nuestra_forma = mapeo_input[input2]

    puntaje = 0

    puntaje += puntaje_por_eleccion[nuestra_forma]

    if rival_forma == nuestra_forma:
        puntaje += puntaje_por_resultado['Empate']
    elif (rival_forma, nuestra_forma) in [('Piedra', 'Papel'), ('Papel', 'Tijera'), ('Tijera', 'Piedra')]:
        puntaje += puntaje_por_resultado['Gano']
    else:
        puntaje += puntaje_por_resultado['Perdio']


    return puntaje

puntaje_acumulado = 0

with open('input') as input:
    for line in input:
        puntaje_acumulado += obtener_puntaje_mapeo(line[0], line[2])

print(f"Puntaje acumulado: {puntaje_acumulado}")

'''

''' 
Part 2
'''
'''
# Mapeamos los inputs con un diccionario

mapeo_input_forma = {'A': 'Piedra', 'B': 'Papel', 'C': 'Tijera'}
mapeo_input_resultado = {'X': 'Perder', 'Y': 'Empatar', 'Z': 'Ganar'}

puntaje_por_eleccion = {'Piedra' : 1, 'Papel': 2, 'Tijera': 3}
puntaje_por_resultado = {'Gano': 6, 'Empate': 3, 'Perdio': 0}

def obtener_nuestra_forma(rival_forma, input_resultado):
    resultado_esperado = mapeo_input_resultado[input_resultado]

    if rival_forma == 'Piedra':
        if resultado_esperado == 'Ganar':
            return 'Papel'
        elif resultado_esperado == 'Perder':
            return 'Tijera'
        else:
            return rival_forma
        
    elif rival_forma == 'Papel':
        if resultado_esperado == 'Ganar':
            return 'Tijera'
        elif resultado_esperado == 'Perder':
            return 'Piedra'
        else:
            return rival_forma
        
    elif rival_forma == 'Tijera':
        if resultado_esperado == 'Ganar':
            return 'Piedra'
        elif resultado_esperado == 'Perder':
            return 'Papel'
        else:
            return rival_forma


def obtener_puntaje(rival_forma, nuestra_forma):
    puntaje = 0
    puntaje += puntaje_por_eleccion[nuestra_forma]

    if rival_forma == nuestra_forma:
        puntaje += puntaje_por_resultado['Empate']
    elif (rival_forma, nuestra_forma) in [('Piedra', 'Papel'), ('Papel', 'Tijera'), ('Tijera', 'Piedra')]:
        puntaje += puntaje_por_resultado['Gano']
    else:
        puntaje += puntaje_por_resultado['Perdio']

    return puntaje

puntaje_acumulado = 0

with open('input') as input:
    for line in input:
        rival_forma = mapeo_input_forma[line[0]]
        nuestra_forma = obtener_nuestra_forma(rival_forma, line[2])
        puntaje_acumulado += obtener_puntaje(rival_forma, nuestra_forma)

print(f"Puntaje acumulado: {puntaje_acumulado}")
'''

# Resolucion : https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-2-with-python/
'''
with open('input-min', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]



map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

def points_per_round(round_string):
    opponent_shape = map_input[round_string[0]]
    our_shape = map_input[round_string[2]]

    if opponent_shape == our_shape:
        return points_per_outcome['Draw'] + points_per_shape[our_shape]
    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        # loss for us
        return points_per_outcome['Lose'] + points_per_shape[our_shape]
    else:
        return points_per_outcome['Win'] + points_per_shape[our_shape]
    

print(sum([points_per_round(round_string) for round_string in rounds]))


'''