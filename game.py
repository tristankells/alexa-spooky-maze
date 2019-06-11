##
## Maze class. Stores a configuration of tiles
##
from grid import Grid
from player import Player

class Game:

    def __init__(self):
        Maze = [
            [['1',0,0,0,0],['Game End',0,1,0,0], ['3',0,0,0,0],['4',0,0,0,0], ['5',0,0,0,0], ['6',0,0,0,0],['7',0,0,0,0]],
            [['8',0,0,0,0],['9',1,1,0,1], ['10',0,0,1,1],['11',0,0,1,1], ['12',0,0,1,1], ['13',0,0,1,1], ['14',0,0,0,0]],
            [['15',0,0,0,0],['16',1,1,0,0], ['17',0,0,0,0],['18',0,0,0,0], ['19',0,0,0,0], ['20',0,0,0,0], ['21',0,0,0,0]],
            [['22',0,0,0,0],['23',1,0,0,1], ['24',0,0,1,1],['25',0,1,1,0], ['26',0,1,1,0], ['27',0,0,0,0], ['28',0,0,0,0]],
            [['29',0,0,0,0],['30',0,0,0,0], ['31',0,0,0,0],['Game Beginning',1,1,0,0], ['33',0,0,0,0], ['34',0,0,0,0], ['35',0,0,0,0]]] 
        Room = []
        self.player = Player(4,1)
        self.maze = Grid(grid_configuration = Maze)
        self.room = Grid(grid_configuration = Maze)

    def move_up(self):
        print("You tried to move up")
        if(self.maze.can_move(self.player.x_coordinate, self.player.y_coordinate, 'up')) :
            print("You moved up")
            self.player.move_up()
        else:
            print("You failed")

    def move_down(self):
        print("You tried to move down")
        if(self.maze.can_move(self.player.x_coordinate, self.player.y_coordinate, 'down')):
            print("You moved down")
            self.player.move_down()
        else:
            print("You failed")

    def move_left(self):
        print("You tried to move left")
        if(self.maze.can_move(self.player.x_coordinate, self.player.y_coordinate, 'left')):
            print("You moved left")
            self.player.move_left()
        else:
            print("You failed")
        

    def move_right(self):
        print("You tried to move right")
        if(self.maze.can_move(self.player.x_coordinate, self.player.y_coordinate, 'right')):
            print("You moved right")
            self.player.move_right()
        else:
            print("You failed")
        

    def handle_input(self, user_input):
        user_input = user_input.lower()
        command_dictionary = {
            'move up' : self.move_up,
            'move down' : self.move_down,
            'move left' : self.move_left,
            'move right': self.move_right
        }
        if user_input not in command_dictionary :
            return lambda : print("Command not recognised. Try again")
        return command_dictionary[user_input]

    def test_player_status(self):
        print("You position is now X = " + str(self.player.x_coordinate) + " Y = " + str(self.player.y_coordinate))
        print("Room Audio: " + self.maze.get_tile(self.player.x_coordinate,self.player.y_coordinate).audio_clip)


    
 
        
game_active = True
game = Game()
game.maze.print_grid()

while(game_active):
    user_input = input()
    game.handle_input(user_input)()
    game.test_player_status()









# Maze = [
# ["0000000","4000000", "0000000", "0000000", "0000000", "0000000", "0000000"],
# ["0000000", "3[1101]", "2[0011]", "0[0011]", "1[0011]", "1[0011]", "0000000"],
# ["0000000", "0[1100]", "0000000", "0000000", "0000000", "0000000", "0000000"],
# ["0000000", "2[1001]", "0[0011]", "1[0011]", "0[0110]", "0000000", "0000000"],
# ["0000000", "0000000", "0000000", "0000000", "1[1100]", "0000000", "0000000"]]
