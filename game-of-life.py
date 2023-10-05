'''
Game of Life
From "Automate the Boring Stuff with Python" by Al Sweigart
'''

import random, time, copy

width = 60
height = 20

# The following creates a list of list for the cells:

next_cells = []

for x in range(width):
    column = [] # creates a new column.
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#') # adds a living cell.
        else:
            column.append(' ') # adds a dead cell.
    next_cells.append(column) # ajb_next_cells is a list of column lists.

# The following is the main program loop.

while True:
    print('\n\n\n\n\n') # separates each step with new lines.
    current_cells = copy.deepcopy(next_cells)
    for y in range(height):
        for x in range(width):
            print(current_cells[x][y], end = '') # prints the current cells on the screen and # or a space.
        print()
    for x in range(width):
        for y in range(height):
            left_coord = (x - 1) % width 
            right_coord = (x + 1) % width 
            up_coord = (y - 1) % height 
            down_coord = (y + 1) % height 
            
            qty_neighbors  = 0
            if current_cells[left_coord][up_coord] == '#':
                qty_neighbors += 1
            if current_cells[x][up_coord] == '#':
                qty_neighbors += 1
            if current_cells[right_coord][up_coord] == '#':
                qty_neighbors += 1
            if current_cells[left_coord][y] == '#':
                qty_neighbors += 1
            if current_cells[right_coord][y] == '#':
                qty_neighbors += 1
            if current_cells[left_coord][down_coord] == '#':
                qty_neighbors += 1
            if current_cells[x][down_coord] == '#':
                qty_neighbors += 1
            if current_cells[right_coord][down_coord] == '#':
                qty_neighbors += 1
            
            if current_cells[x][y] == '#' and (qty_neighbors == 2 or qty_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and qty_neighbors == 3:
                next_cells[x][y]= '#'
            else:
                next_cells[x][y] = ' '
    time.sleep(1)