##
## Player class. Store the x and y coordinates of the player. Has functions for moving in all four directions 
##
class Player:
    ##Player constructor. Take x and y coordinates for the maze
    def __init__(self, x_coordinate,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def move_up(self):
        self.y_coordinate += 1

    def move_down(self):
        self.y_coordinate -= 1

    def move_right(self):
        self.x_coordinate += 1

    def move_left(self):
        self.x_coordinate -= 1

        ##For tests
    def get_coordinates(self):
        print('My current position is X = ' + str(self.x_coordinate) + ' AND Y = ' +  str(self.y_coordinate))

##
## Class Test
##
p1 = Player(0,0)
p1.move_up()
p1.get_coordinates()
