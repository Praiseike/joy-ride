import os
import horse
import pygame
import renderer
import gameObject
import background
import eventHandler
import audioManager

class Game(object):
    """ The main game Class"""

    g_renderer = None
    running = True

    def __init__(self,window_name,window_size=(900,600)):
        self.window_name = window_name
        self.window_size = window_size
        self.window = pygame.display.set_mode(window_size,pygame.DOUBLEBUF,32)
        self.screen = pygame.Surface(window_size,pygame.SRCALPHA,32)
        pygame.display.set_caption(self.window_name)
        self.g_renderer = renderer.Render(self.screen)
        player = horse.Horse(pygame.Rect(200,460,0,0))
        back = background.Background()
        self.g_renderer.register_object(back,player)
        self.handle = eventHandler.EventHandler(player)
        self.audio_manager = audioManager.AudioManager()
        self.audio_manager.register_music("assets/audio/car-racing-computer-game_WM.ogg")
        self.audio_manager.play_music()
        return

    def update(self):
        self.window.fill((160,160,160))
        self.g_renderer.draw_objects()
        self.window.blit(self.screen,pygame.rect.Rect(0,0,0,0))
        pygame.display.update()
        return


    def die(self):
        print("Exiting")
        pygame.quit()
        return

    def mainloop(self):
        while(self.running):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.running = False

            self.handle.handle_keys()
            self.update()
        
        self.die()
        return
