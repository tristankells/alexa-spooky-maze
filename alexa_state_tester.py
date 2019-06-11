##
## Games class. Store a player object
##
from game import Game



  
state_variables = {
    'coordinates' : {
        'x' : 5,
        'y' : 1
    }
}



game_active = True
while(game_active):
    user_input = input()
    fresh_game = Game(state_variables)
    fresh_game.handle_input(user_input)()
    state_variables = fresh_game.get_state_variables()








    
 
        

