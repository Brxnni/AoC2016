from   pygame import mixer
mixer.init()

def play(path: str):
    mixer.music.load(path)
    mixer.music.play()