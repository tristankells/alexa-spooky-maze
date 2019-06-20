# Player class. Store the x and y coordinates of the player. Methods for moving
# in north, south, west and east
class Player:
    #Player constructor. Take x and y coordinates for the maze
    def __init__(self,coordinates):
        self.x_coordinate = coordinates['x']
        self.y_coordinate = coordinates['y']

    def set_coordinates(self, coordinates) :
        self.x_coordinate = coordinates['x']
        self.y_coordinate = coordinates['y']

    # Adjust the player coordinates based on string input of a cardinal 
    # direction ('north', 'west', etc..)
    def move(self, movement) :
        move_dictionary = {
            'north' : self.move_north,
            'south' :self.move_south,
            'west' : self.move_west,
            'east' : self.move_east
        }
        move_dictionary[movement]()


    def move_north(self):
        self.y_coordinate += 1

    def move_south(self):
        self.y_coordinate -= 1

    def move_west(self):
        self.x_coordinate -= 1

    def move_east(self):
        self.x_coordinate += 1