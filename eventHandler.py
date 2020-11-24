
import pygame

class EventHandler(object):

    def __init__(self,horse_obj):
        self.horse = horse_obj

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_SPACE] or keys[pygame.K_UP]):
            self.horse.isjump = True
        if(keys[pygame.K_F11]):
            pygame.display.toggle_fullscreen()
        return