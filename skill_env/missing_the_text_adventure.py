
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
        game = Game()

        print(Translator(game.handle_launch_input()))

        while(self.game_active):

            user_input = input()

            game.setup(self.state_variables)

            print(Translator(game.handle_move_input(user_input)))

            self.save(game.game_variables())

            

missing_the_text_adventure().play()
