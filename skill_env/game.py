##
## Games class. Store a player object
##
from grid import Grid
from player import Player
from audio import Audio





class Game:

    def __init__(self, state_variables):
        # Maze = [
        #     [{"code" : 'wall'}, {"code" : 'outr'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'wall'},{"code" : 'wall'}, {"code" : 'wall'}],
        #     [{"code" : 'wall'}, {"code" : 'foot'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'wall'},{"code" : 'wall'}, {"code" : 'wall'}],
        #     [{"code" : 'wall'}, {"code" : 'foot'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'wall'},{"code" : 'wall'}, {"code" : 'wall'}],
        #     [{"code" : 'wall'}, {"code" : 'foot'},{"code" : 'foot'}, {"code" : 'foot'}, {"code" : 'foot'},{"code" : 'wall'}, {"code" : 'wall'}],
        #     [{"code" : 'wall'}, {"code" : 'wall'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'into'},{"code" : 'wall'}, {"code" : 'wall'}]]

        Maze = [
           ['wall', 'end', 'wall', 'wall', 'star', 'wall', 'wall'],
           ['wall', 'foot', 'loud', 'meds', 'foot', 'meds', 'wall'],
           ['wall', 'loud', 'wall', 'wall', 'wall', 'wall', 'wall'],
           ['wall', 'meds', 'foot', 'quis', 'quis', 'wall', 'wall'],
           ['wall', 'wall', 'wall', 'wall', 'star', 'wall', 'wall']]

        Puzzle_Room = [
            ['wall', 'end', 'wall', 'wall', 'star', 'wall', 'wall'],
           ['wall', 'foot', 'loud', 'meds', 'foot', 'meds', 'wall'],
           ['wall', 'loud', 'wall', 'wall', 'wall', 'wall', 'wall'],
           ['wall', 'meds', 'foot', 'quis', 'quis', 'wall', 'wall'],
           ['wall', 'wall', 'wall', 'wall', 'star', 'wall', 'wall']
        ]
       
         
        self.player = Player(state_variables['coordinates'])
        self.maze = Grid(grid_configuration = Maze)
        self.puzzle_room = Grid(grid_configuration = Puzzle_Room)

    def move(self, movement) :
        new_room_code = self.maze.get_new_room_code(self.player.x_coordinate, self.player.y_coordinate, movement)
        
        if(new_room_code != 'wall') :
            self.player.move(movement)

        return new_room_code
        
        

    def handle_move_input(self, user_input):
        response_audio = ""
        room_code = ""
        user_input = user_input.lower()
        command_dictionary = {
            'forward' : self.move('north'),
            'back' : self.move('south'),
            'left' : self.move('west'),
            'right': self.move('east')
        }
        
        room_code = command_dictionary[user_input]

        response_audio = speech_text_library(room_code)

        return response_audio

        
    def print_player_status(self):
        print("You position is now X = " + str(self.player.x_coordinate) + " Y = " + str(self.player.y_coordinate))
        print("Room Audio: " + self.maze.get_tile(self.player.x_coordinate,self.player.y_coordinate).audio_clip)

    def get_game_variables(self):
        return {'coordinates' : {
            'x' : self.player.x_coordinate , 
            'y': self.player.y_coordinate
        }}
    

    
def speech_text_library(selection) :
    library = {
        'into' : "Welcome to Saving Shiraz Beta" + Audio('intro'),
        'exit' : Audio('outro'),
        'quie' : Audio('footsteps') + Audio('quiet shiraz'),
        'medi' : Audio('footsteps') + Audio('medium shiraz'),
        'loud' : Audio('footsteps') + Audio('loud shiraz'),
        'wall' : Audio('wall')
    }
    return library[selection]
