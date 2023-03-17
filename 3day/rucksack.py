'''
--- Day 3: Rucksack Reorganization ---
'''


'''
Part 1
'''
'''

def find_repeated_item(rucksack):
    #str_len = len(rucksack)
    #first_compartment = str[0:str_len//2]
    #second_compartment = str[str_len//2:]
    first_compartment, second_compartment = rucksack[0:len(rucksack)//2], rucksack[len(rucksack)//2:]

    #print(f"{first_compartment}, {second_compartment}")
    
    for char in first_compartment:
        if char in second_compartment:
            return char


#repeated_item = find_repeated_item('vJrwpWtwJgWrhcsFMMfFFhFp')

#print(repeated_item)

elementos_repetidos = []

with open('input') as file:
    for line in file:
        char = find_repeated_item(line.strip())
        elementos_repetidos.append(char)

#print(elementos_repetidos)

suma_de_prioridades = 0
for item in elementos_repetidos:
    if item.islower():
        suma_de_prioridades += ord(item) - ord('a') + 1
    else:
        suma_de_prioridades += ord(item) - ord('A') + 27

print(f"Valor: {suma_de_prioridades}")


'''
'''
Part 2
'''

# Cargamos el archivo en memoria

with open('input') as file:
    lines = file.readlines()
    rucksacks = [line.strip() for line in lines]

# Función para comparar 3 mochilas

def find_repeated_badge(first, second, third):
    for item in first:
        if item in second:
            if item in third:
                return item

def get_priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

priority_sum = 0
while len(rucksacks) > 0:
    group_list = []
    for i in range(3):
        group_list.append(rucksacks.pop(0))
    badge = find_repeated_badge(group_list[0], group_list[1], group_list[2])
    priority_sum += get_priority(badge)

print(f"Valor: {priority_sum}")



