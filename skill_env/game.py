

from room import Room
from player import Player
from audio import Audio

# Games class. Store a player object
# MemberVariables :
#   code : A string of characters representing the room event (audio file etc..)
class Game:

    Maze = [
             [{"code" : 'wall'}, {"code" : 'exit'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'star'},{"code" : 'wall'}, {"code" : 'wall'}],
             [{"code" : 'wall'}, {"code" : 'foot'},{"code" : 'loud'}, {"code" : 'meds'}, {"code" : 'foot'},{"code" : 'meds'}, {"code" : 'wall'}],
             [{"code" : 'wall'}, {"code" : 'loud'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'wall'},{"code" : 'wall'}, {"code" : 'wall'}],
             [{"code" : 'wall'}, {"code" : 'meds'},{"code" : 'foot'}, {"code" : 'quis'}, {"code" : 'quis'},{"code" : 'wall'}, {"code" : 'wall'}],
             [{"code" : 'wall'}, {"code" : 'wall'},{"code" : 'wall'}, {"code" : 'wall'}, {"code" : 'star'},{"code" : 'wall'}, {"code" : 'wall'}]]

    def __init__(self, game_dict): 
        self.player = Player(game_dict['coordinates'])
        self.maze = Room(self.Maze)


    def move(self, movement) :
        new_tile_code = self.maze.get_new_tile(self.player.x_coordinate, self.player.y_coordinate, movement).code
        
        if(new_tile_code != 'wall') :
            self.player.move(movement)

        return new_tile_code
        
        

    def handle_move_input(self, user_input):
        response_audio = ""
        room_code = ""
        user_input = user_input.lower()
        command_dictionary = {
            'forward' : 'north',
            'back' : 'south',
            'left' : 'west',
            'right': 'east'
        }
        
        room_code = self.move(command_dictionary[user_input])

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
        'quis' : Audio('footsteps') + Audio('quiet shiraz'),
        'meds' : Audio('footsteps') + Audio('medium shiraz'),
        'loud' : Audio('footsteps') + Audio('loud shiraz'),
        'wall' : Audio('wall'),
        'foot' : Audio('footsteps')
    }
    return library[selection]
