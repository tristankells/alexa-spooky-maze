##
## Tile class. Represnts space in either room or the maze. Store the walls 
##
class Tile:
    ##Player constructor. Take x and y coordinates for the maze
    def __init__(self, audio_clip):
        self.audio_clip = audio_clip
        
        ##For tests
    def print_tile(self):
        print("Audio : " + self.audio_clip + "Walls ")
    
    def wall_to_int(self, wall) :
        return '0' if wall else '1'
    
        
           
# #Test a Creating a Room
# T1 = Tile(True,False,True,True, "quiet shiraz")
# T1.print_tile()

