from tile import Tile

# Room class. Stores a 2 dimenstional configuration of tiles. Representt the different rooms of game (Maze room or Puzzle room)
# MemberVariables :
#   room : A 2 dimentional list of tiles
class Room:
    
    # Room constructor. Take a room configuration  
    def __init__(self, room_list):
        room = []

        # For each list of tiles in the room list, append a list 
        for tile_row_list in room_list:
            room.append(self.get_tile_row(tile_row_list))

        self.room = room

    def get_tile_row(self, tile_dict_list):
        room_row = []
        for tile_dict in tile_dict_list:
            room_row.append(Tile(tile_dict))
        return room_row

    def get_tile(self, x_coordinate, y_coordinate):
        return self.room[-y_coordinate][x_coordinate-1]

    def get_new_tile(self, x_coordinate, y_coordinate, direction) :
        if(direction == 'north'):  return self.get_tile(x_coordinate, y_coordinate + 1)
        elif(direction == 'south'): return self.get_tile(x_coordinate, y_coordinate - 1)
        elif(direction == 'west'): return self.get_tile(x_coordinate -1, y_coordinate)
        elif(direction == 'east'): return self.get_tile(x_coordinate + 1, y_coordinate)