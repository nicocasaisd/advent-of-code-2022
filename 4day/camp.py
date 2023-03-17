'''
--- Day 4: Camp Cleanup ---
'''

# Cargamos el archivo en una lista de pares

with open('input') as file:
    lines = file.readlines()
    pairs = [line.strip() for line in lines]

# Funcion para transformar las entradas en sets
def generate_sets(pair):
    a, b = pair.split(',')
    range_bounds = [a.split('-'), b.split('-')]
    set1 = set(range(
        int(range_bounds[0][0]), int(range_bounds[0][1])+1
        ))
    set2 = set(range(
        int(range_bounds[1][0]), int(range_bounds[1][1])+1
        ))

    return set1, set2


# Calculamos la cantidad de sets totalmente superpuestos

number_of_pairs_overlapped = 0

for item in pairs:
    set1, set2 = generate_sets(item)
    if set1.issubset(set2) or set2.issubset(set1):
        number_of_pairs_overlapped += 1


print(f"Cantidad de sets superpuestos totalmente: {number_of_pairs_overlapped}")

'''
Part 2
'''

# Calculamos la cantidad de sets superpuestos total o parcialmente

number_of_pairs_overlapped = 0

for item in pairs:
    set1, set2 = generate_sets(item)
    if set1 & set2:
        number_of_pairs_overlapped += 1


print(f"Cantidad de sets superpuestos parcialmente: {number_of_pairs_overlapped}")