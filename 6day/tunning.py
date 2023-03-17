'''
--- Day 6: Tuning Trouble ---
'''

FILE_NAME = 'input'

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
        