def Translator(code) :
    text_translator = {
        'into' : "into : Welcome to Saving Shiraz Beta You arrive home. Your" + 
        "son missing... fuck, guess dinner gonna have to wait",
        'exit' : "exit : Game Over???",
        'quis' : 'quis: you can kinda hear someone crying',
        'meds' : 'meds : You can hear someone yealling mediumy',
        'loud' : 'loud: YOU CAN HEAR SOMEONE CRYING REALLY CLOSE BY',
        'wall' : 'wall: Straight into a wall, like a dumbass',
        'foot' : 'foot: Just some footsteps'
    }
    return text_translator[code]