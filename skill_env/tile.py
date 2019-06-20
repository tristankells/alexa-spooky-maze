
# Class : Tile 
#   Represnts space in either room or the maze. Store a code, which 
#   represents an audio file and is used to indicate if certain actions can 
#   take within the tile (Turn on tractor etc...)

# MemberVariables :
#   code : A string of characters representing the room event (audio file etc..)
#   
class Tile:
    # Tile constructor()
    # Take a dictonary which contains room attributes
    #  
    def __init__(self, tile_dict):
        self.code = tile_dict['code']