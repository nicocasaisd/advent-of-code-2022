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
    lines = [line.strip() for line in lines]

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
        self.parent=None

    # Todos son métodos de instancia, por eso reciben 'self'
    def add_child(self, child):
        # Asigno el atributo parent para que se relacione con esta instancia
        child.parent = self
        self.children.append(child)

    def get_size(self):
        # Si es un directorio
        if self.is_dir:
            total_size = 0 # acumulador
            # recorre todos los children
            for child in self.children:
                total_size += child.get_size()
            return total_size
        # Si es un archivo
        else:
            return self.size
        
    def print_children(self, level):
        if self.is_dir:
            print('--' * level + self.name + '(total=' + str(self.get_size()) + ')')
        else:
            print('--' * level + self.name + '(file=' + str(self.get_size()) + ')')
        
        if len(self.children)>0:
            for child in self.children:
                child.print_children(level+1)

# Clase árbol que contiene los Nodes
class Tree:
    def __init__(self) -> None:
        self.root = Node(is_dir=True, name='root')
        self.current = self.root

    def reset_to_root(self):
        self.current = self.root

    def go_up_one_level(self):
        self.current = self.current.parent

    def go_to_child(self, name):

        for child in self.current.children:
            if child.name == name:
                self.current = child
                return
            
    def add_new_child(self, child):
        self.current.add_child(child)

    
# Programa

tree = Tree()

# Loop while general
while len(lines)>0:
    entry = lines.pop(0) # popeamos la linea en index=0

    if '$ cd /' in entry:
        tree.reset_to_root()
    elif '$ ls' in entry:
        while '$' not in lines[0]:
            entry = lines.pop(0)
            size, name = entry.split(' ')
            if size.isdigit():
                new_node = Node(is_dir=False, name=name, size=size)
            else:
                new_node = Node(is_dir=True, name=name)
            tree.add_new_child(new_node)
    elif '$ cd ..' in entry:
        tree.go_up_one_level()
    elif 'cd' in entry:
        # tomamos el nombre del directorio
        _,_,name = entry.split(' ')
        tree.go_to_child(name)
    
    tree.root.print_children(0)
        
tree.root.print_children(0)

        
    
        


