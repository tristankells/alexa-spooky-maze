##
## Games class. Store a player object
##
from game import Game



  
state_variables = {
    'coordinates' : {
        'x' : 2,
        'y' : 4
    }
}



game_active = True
while(game_active):
    user_input = input()
    fresh_game = Game(state_variables)
    print(fresh_game.handle_move_input(user_input))
    state_variables = fresh_game.get_game_variables()
    print(str(state_variables['coordinates']['x']) + ' AND ' + str(state_variables['coordinates']['y']))








    
 
        

