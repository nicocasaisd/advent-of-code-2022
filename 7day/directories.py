'''
--- Day 7: No Space Left On Device ---
'''

'''
Part 1
'''
import re


# Leemos el archivo input

FILE_NAME = 'input-min'

with open(FILE_NAME) as file:
    lines = file.readlines()
    #lines = [line.strip() for line in lines]

# root = []

# for line in lines:
#     if 'dir' in line:
#         dir_name = re.sub("\(.*?\)","",line)
#         root.append({dir_name:[]})

# Creamos una clase Nodo

class Node:
    # Constructor de clase
    def __init__(self, is_dir:bool, name:str, size=None) -> None:
        # atributos
        self.is_dir = is_dir
        self.name = name
        self.size = size
        self.children = []

    

    
    
        


