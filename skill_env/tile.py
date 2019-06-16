##
## Tile class. Represnts space in either room or the maze. Store the walls 
##
class Tile:
    ##Player constructor. Take x and y coordinates for the maze
    def __init__(self, code):
        self.code = code
        
        ##For tests
    def print_tile(self):
        print("Audio : " +  self.code )
    

    
        
           
# #Test a Creating a Room
# T1 = Tile(True,False,True,True, "quiet shiraz")
# T1.print_tile()

