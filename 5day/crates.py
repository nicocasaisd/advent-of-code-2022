'''
--- Day 5: Supply Stacks ---
'''

# Leemos el archivo

FILE_NAME = 'input'

starting_arr = []

with open(FILE_NAME) as file:
    while True:
        line = file.readline()
        
        if line != '\n':
            starting_arr.append(line)
        else:
            break

# Leemos la disposición inicial de cajas

list_of_stacks = []
length_of_line = len(starting_arr[0])

for index in range(length_of_line):
    if starting_arr[len(starting_arr)-1][index].isnumeric():
        stack_aux = []
        for j in reversed(range(len(starting_arr))):
            if starting_arr[j][index] != ' ':
                stack_aux.append(starting_arr[j][index])
        list_of_stacks.append(stack_aux)

#print(list_of_stacks)

# Funcion para mover las cajas

def move_crates(from_stack, to_stack, number):
    for i in range(number):
        to_stack.append(from_stack.pop())

#move_crates(list_of_stacks[1], list_of_stacks[2], 2)
#print(list_of_stacks)

# Leemos las instrucciones

with open(FILE_NAME, 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

instructions = lines[lines.index('\n')+1:]
# .index() devuelve el indice de la primera aparicion del argumento pasado

#print(instructions)

# Obtenemos los valores deseados

def get_instruction_values(line):
    return_values = []
    for entry in line.strip().split(' '):
        if entry.isdigit():
            return_values.append(int(entry))
    
    return return_values

#print(get_instruction_values(instructions[0]))

# Ejecutamos todas las instrucciones con un loop
'''
for line in instructions:
    number, from_index, to_index = get_instruction_values(line)
    move_crates(list_of_stacks[from_index-1], list_of_stacks[to_index-1], number)
'''
#print(list_of_stacks)

# Mostramos el resultado

""" print(f"El resultado es: ")

for column in range(len(list_of_stacks)):
    print(list_of_stacks[column].pop(),end='')

print('') """

'''
Parte 2
'''

# Funcion para mover las cajas de a muchas

def move_crates_multiple(from_stack, to_stack, number):
    if number > 1:
        for i in range(-number,0,1):
            to_stack.append(from_stack.pop(i))
    else:
        to_stack.append(from_stack.pop())


# Ejecutamos todas las instrucciones con un loop

for line in instructions:
    number, from_index, to_index = get_instruction_values(line)
    move_crates_multiple(list_of_stacks[from_index-1], list_of_stacks[to_index-1], number)

# Mostramos el resultado

print(f"El resultado es: ")

for column in range(len(list_of_stacks)):
    print(list_of_stacks[column].pop(),end='')

print('')