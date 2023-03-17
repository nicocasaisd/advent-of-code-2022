'''
--- Day 6: Tuning Trouble ---
'''

FILE_NAME = 'input-min'

with open(FILE_NAME) as file:
    datastream = file.readline()

'''
PART 1
'''
for i in enumerate(datastream):
    marker = True
    if i[0] > 3:
        buffer = datastream[i[0]-4:i[0]]
        for item in buffer:
            if buffer.count(item) > 1:
                marker = False
                break
        
        if marker:
            print(i)
            break
        
    
'''
PART 2
'''


for i in enumerate(datastream):
    marker = True
    if i[0] > 13:
        buffer = datastream[i[0]-14:i[0]]
        for item in buffer:
            if buffer.count(item) > 1:
                marker = False
                break
        
        if marker:
            print(i)
            break
        

'''
Solution from https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-6-with-python/
'''

# It is shorter and uses a set to check if duplicate values exist

for i in range(len(datastream)):
    if len(set(datastream[i:i+4]))==4:
        print(i+4)
        break
