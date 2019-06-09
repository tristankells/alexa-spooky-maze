##
## Tile class. Represnts space in either room or the maze. Store the walls 
##
class Tile:
    ##Player constructor. Take x and y coordinates for the maze
    def __init__(self, north_wall , east_wall, south_wall, west_wall, audio_clip):
        self.north_wall = north_wall
        self.east_wall = east_wall
        self.south_wall = south_wall
        self.west_wall = west_wall
        self.audio_clip = audio_clip
        
        ##For tests
    def print_tile(self):
        room_string = ""
        if(self.north_wall == True) :
            room_string += ' _'
        if(self.west_wall == True) :
            room_string += '|'
        if(self.south_wall == True) :
            room_string += '_'
        else:
            room_string += ' '
        if(self.east_wall == True) :
            room_string += '|'

        print(room_string)
        
           
# #Test a Creating a Room
# T1 = Tile(True,True,True,True, "quiet shiraz")
# T1.print_tile()

