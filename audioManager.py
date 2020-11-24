import time
from pygame import mixer

class AudioManager(object):
    sound_store = {}

    def __init__(self):
        self.name = "audiomanager"
        mixer.init(44100)

    def register_music(self,filename,vol=0.7):
        mixer.music.load(filename)
        mixer.music.set_volume(vol)

    def register_sound(self,filename,id):
        self.sound_store[id] = mixer.Sound(filename)
    
    def play_music(self):
        mixer.music.play(-1,0.0)

    def play_sound(self,id):
        self.sound_store[id].play()

    def pause_sound(self,id):
        self.sound_store[id].pause()

    def die(self):
        mixer.quit()
