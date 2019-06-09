##
## Maze class. Stores a configuration of tiles
##
from tile import Tile

class Grid:

    def __init__(self, grid_configuration):
        self.grid = self.grid_constructor(grid_configuration)
        
 

    def tile_constructor(self, tile_configuration):
        audio_clip = tile_configuration[0]
        north_wall = True if (tile_configuration[1] == 1) else False
        south_wall = True if (tile_configuration[2] == 1) else False
        west_wall = True if (tile_configuration[3] == 1) else False
        east_wall = True if (tile_configuration[4] == 1) else False

        return Tile(north_wall, east_wall, south_wall , west_wall, audio_clip)

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
            print(tile.print_tile())

    def print_grid(self):
        for row in self.grid:
            print(self.print_row(row))





        
Maze = [
[['',0,0,0,0],['',0,0,0,0], ['',0,0,0,0],['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0],['',0,0,0,0]],
[['',0,0,0,0],['',1,1,0,1], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',1,1,0,0], ['',0,0,0,0]],
[['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]],
[['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]],
[['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]]] 

#Test a Creating a Room
G1 = Grid(grid_configuration = Maze)
G1.print_grid()


# Maze = [
# ["0000000","4000000", "0000000", "0000000", "0000000", "0000000", "0000000"],
# ["0000000", "3[1101]", "2[0011]", "0[0011]", "1[0011]", "1[0011]", "0000000"],
# ["0000000", "0[1100]", "0000000", "0000000", "0000000", "0000000", "0000000"],
# ["0000000", "2[1001]", "0[0011]", "1[0011]", "0[0110]", "0000000", "0000000"],
# ["0000000", "0000000", "0000000", "0000000", "1[1100]", "0000000", "0000000"]]

# Maze = [
# ["0000000","4000000", "0000000", "0000000", "0000000", "0000000", "0000000"],
# ["0000000", "3[1101]", "2[0011]", "0[0011]", "1[0011]", "1[0011]", "0000000"],
# ["0000000", "0[1100]", "0000000", "0000000", "0000000", "0000000", "0000000"],
# ["0000000", "2[1001]", "0[0011]", "1[0011]", "0[0110]", "0000000", "0000000"],
# ["0000000", "0000000", "0000000", "0000000", "1[1100]", "0000000", "0000000"]]

