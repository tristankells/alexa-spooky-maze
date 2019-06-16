##
## Maze class. Stores a configuration of tiles
##
from tile import Tile

class Grid:

    ##
    ##Grid contructor
    ##
    def __init__(self, grid_configuration):
        self.grid = self.grid_constructor(grid_configuration)

    ##
    ## Takes a list in the form ['quiet noise', 1, 1, 0 , 1] for example and constructs a tile.
    ##
    def tile_constructor(self, tile_configuration):
        audio_clip = tile_configuration[0]

        return Tile( audio_clip)

    def row_constructor(self, row_configuration):
        grid_row = []
        for tile_configuration in row_configuration:
            grid_row.append(self.tile_constructor(tile_configuration))
        return grid_row

    def grid_constructor(self, grid_confirguation):
        grid = []
        for row_configuration in grid_confirguation:
            grid.append(self.row_constructor(row_configuration))
        return grid
    
    def print_row(self, row):
        for tile in row:
            tile.print_tile()
        print(' ')

    def print_grid(self):
        for row in self.grid:
            self.print_row(row)
    
    def get_tile(self, x_coordinate, y_coordinate):
        return self.grid[-y_coordinate][x_coordinate-1]

    def get_new_room_code(self, x_coordinate, y_coordinate, direction) :
        if(direction == 'north'):  return self.get_tile(x_coordinate, y_coordinate + 1)
        elif(direction == 'south'): return self.get_tile(x_coordinate, y_coordinate - 1)
        elif(direction == 'west'): return self.get_tile(x_coordinate -1, y_coordinate)
        elif(direction == 'east'): return self.get_tile(x_coordinate + 1, y_coordinate)
        
    
    

        
            
        





        
# Maze = [
# [['',0,0,0,0],['',0,0,0,0], ['',0,0,0,0],['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0],['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,1], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',1,1,0,0], ['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]]] 

# #Test a Creating a Room
# G1 = Grid(grid_configuration = Maze)
# G1.print_grid()


# 
# Oringinal maze li 
#

