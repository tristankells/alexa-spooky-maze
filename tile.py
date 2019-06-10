##
## Tile class. Represnts space in either room or the maze. Store the walls 
##
class Tile:
    ##Player constructor. Take x and y coordinates for the maze
    def __init__(self, north_wall , south_wall, west_wall, east_wall, audio_clip):
        self.north_wall = north_wall
        self.south_wall = south_wall
        self.west_wall = west_wall
        self.east_wall = east_wall
        self.audio_clip = audio_clip
        
        ##For tests
    def print_tile(self):
        print("Audio : " + self.audio_clip + " Walls : " + self.wall_to_int(self.north_wall) + self.wall_to_int(self.south_wall) + self.wall_to_int(self.west_wall) + self.wall_to_int(self.east_wall), end=" ")
    
    def wall_to_int(self, wall) :
        return '1' if wall else '0'
    
        
           
# #Test a Creating a Room
# T1 = Tile(True,False,True,True, "quiet shiraz")
# T1.print_tile()

