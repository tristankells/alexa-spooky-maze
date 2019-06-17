
from game import Game
from text_translator import Translator

# Games class. Store a player object
class missing_the_text_adventure :
    # Map room code to texts reponse, 
  

    state_variables = {
    'coordinates' : {
        'x' : 5,
        'y' : 1
        }
    }

    def save(self, game_variables) :
        self.state_variables = game_variables

    game_active = True

    def play(self) :
        print(Translator('into'))
        while(self.game_active):
            user_input = input()
            fresh_game = Game(self.state_variables)
            game_response = fresh_game.handle_move_input(user_input)
            self.save(fresh_game.get_game_variables())
            print(Translator(game_response))

missing_the_text_adventure().play()
