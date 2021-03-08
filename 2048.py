"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    funktion used for merge hui
    """
    length = len(line)
    num = 0
    baffer = 0
    new_line = []
    while num < length:
        if line[num] > 0:
            if baffer == 0:  
                baffer = line[num]
            else:
                if baffer == line[num]:
                    new_line.append(baffer*2)
                    baffer = 0
                else:
                    new_line.append(baffer)
                    baffer = line[num]
        num = num +1    
    if baffer > 0:
        new_line.append(baffer) 
    while len(new_line) < length:
        new_line.append(0)
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.cell_value = []
        pass

    def reset(self):
        self.cell_value = [[0 for col in range(self.grid_width)]
                           for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        return "hui"

    def get_grid_height(self):
        return self.grid_height

    def get_grid_width(self):
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        if direction == 1:
            for row in range(self.grid_width):
                line1 = [self.get_tile(col,row) for col in range(self.grid_height)]
                line1 = merge(line1)
                for lol in range(self.grid_height):
                    self.set_tile(lol,row,line1[lol])
                    
        compute_line = [self.get_tile(starto[1]+line*OFFSETS[1],starto[0]+line*OFFSETS[0]) for line in range(start_line_length)]
            print compute_line
            compute_line = merge(compute_line)
            for lol in range(start_line_length):
                    self.set_tile(starto[1]+lol,starto[0],compute_line[lol])
        """
        if direction == 1:
            start_cells = [[row,0] for row in range(self.grid_width)]
            start_line_length = self.grid_height
        elif direction == 2:      
            start_cells = [[row,self.grid_height-1] for row in range(self.grid_width)]
            start_line_length = self.grid_height
        elif direction == 3:
            start_cells = [[0,row] for row in range(self.grid_height)]
            start_line_length = self.grid_width
        elif direction == 4:
            start_cells = [[self.grid_width-1,row] for row in range(self.grid_height)]
            start_line_length = self.grid_width
        for starto in start_cells:
            compute_line = [self.get_tile(starto[1]+line*OFFSETS[direction][0],starto[0]+line*OFFSETS[direction][1]) for line in range(start_line_length)]
            compute_line = merge(compute_line)
            for lol in range(start_line_length):
                    self.set_tile(starto[1]+lol*OFFSETS[direction][0],starto[0]+lol*OFFSETS[direction][1],compute_line[lol])
            
        self.new_tile()               

    def new_tile(self):
        column = random.randrange(0, self.grid_width)
        row = random.randrange(0, self.grid_height)
        if self.get_tile(row,column) == 0:
            #self.cell_value[row][column] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
            self.set_tile(row,column,random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]))
        else: 
            self.new_tile()


    def set_tile(self, row, col, value):
        self.cell_value[row][col] = value
        pass

    def get_tile(self, row, col):
        return self.cell_value[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
