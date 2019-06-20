from audio import Audio

def Translator(code) :
    text_translator = {
        'into' : "Welcome to Saving Shiraz. Use your voice to navigate using " + 
            "the commands: move forward, move back, move right, or move left. " + 
            "Follow your son’s voice and watch out for walls and dead ends. Good luck" 
            + Audio('intro'),
        'exit' : Audio('outro'),
        'quis' : Audio('footsteps') + Audio('quiet shiraz'),
        'meds' : Audio('footsteps') + Audio('medium shiraz'),
        'loud' : Audio('footsteps') + Audio('loud shiraz'),
        'wall' : Audio('wall'),
        'foot' : Audio('footsteps')
    }    
    return text_translator[code]

   
