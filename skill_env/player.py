##
## Player class. Store the x and y coordinates of the player. Has functions for moving in all four directions 
##
class Player:
    ##Player constructor. Take x and y coordinates for the maze
    def __init__(self,coordinates):
        self.x_coordinate = coordinates['x']
        self.y_coordinate = coordinates['y']

    def set_coordinates(self, coordinates) :
        self.x_coordinate = coordinates['x']
        self.y_coordinate = coordinates['y']


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

# ##
# ## Class Test
# ##
# p1 = Player({'x' : 4, 'y' : 1})
# p1.move_up()
# p1.get_coordinates()
# p1.move_down()
# p1.get_coordinates()
# p1.move_left()
# p1.get_coordinates()
# p1.move_right()
# p1.get_coordinates()