from audio import Audio

def Translator(code) :
    text_translator = {
       'into' : "Welcome to Saving Shiraz Beta" + Audio('intro'),
        'exit' : Audio('outro'),
        'quis' : Audio('footsteps') + Audio('quiet shiraz'),
        'meds' : Audio('footsteps') + Audio('medium shiraz'),
        'loud' : Audio('footsteps') + Audio('loud shiraz'),
        'wall' : Audio('wall'),
        'foot' : Audio('footsteps')
    }    
    return text_translator[code]

   
