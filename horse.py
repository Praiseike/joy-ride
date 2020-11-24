import pygame
import gameObject
import audioManager

class Horse(gameObject.GameObject):
    normal_sprites_path = ["assets/horse/%i.png"%i for i in range(1,8)] # 1.png,2.png,3.png ... 7.png
    jump_sprites_path = ["assets/horse/jump/1.png","assets/horse/jump/2.png"]
    normal_sprites = []
    jump_sprites = []
    isjump = False
    jump_height = 7

    def __init__(self,image_rect):
        self.audio_manager = audioManager.AudioManager()
        self.audio_manager.register_sound("assets/audio/gallop.ogg","gallop")
        self.audio_manager.play_sound("gallop")
        gameObject.GameObject.__init__(self,self.normal_sprites_path[0],image_rect)
        self.prev_pos = self.pos.copy()
        self.t_index = 0
        self.t_max = len(self.normal_sprites)
        try:
            for i in self.normal_sprites_path:
                self.normal_sprites.append(pygame.image.load(i).convert_alpha())
            for i in self.jump_sprites_path:
                self.jump_sprites.append(pygame.image.load(i).convert_alpha())
        except Exception as e:
            print(e)


    def draw_normal(self,screen):
        if(self.t_index >= 6):
            self.t_index = 0
        self.image = self.normal_sprites[self.t_index]
        screen.blit(self.image,self.pos)
        self.t_index +=1

    def jump_test1(self):
        if(self.jump_height >= -8):
            self.audio_manager.pause_sound("gallop")
            self.pos.top -= (self.jump_height * abs(self.jump_height)*0.5)
            self.jump_height -= 3
        else:
            self.jump_height = 8
            self.pos = self.prev_pos.copy()
            self.isjump = False
            self.audio_manager.play_sound("gallop.ogg")

    def draw(self,screen):
        if(self.isjump):
            self.jump_test1()
        self.draw_normal(screen)
        pygame.time.delay(50)
