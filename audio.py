def get_audio_element(audio_selection):
    switcher = {
       'intro': "Into", 
       'quiet shiraz': "Quiet+Shiraj",
       'medium shiraz': "Medium+Shiraj",
       'loud shiraz': "Loud+shiraj", 
       'hiting a wall': "Hitting+a+wall",
       'footsteps': "footsteps",
       'outro': "Outro"
    }
    return ("<audio src='https://s3.amazonaws.com/alexa-alexa-sound/" + switcher.get(audio_selection,) +  ".mp3'/>") 