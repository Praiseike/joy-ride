import pygame,os
from pygame.locals import *

class GameObject(object):
    """ This the main game object class all active 
        elements will inherit from
    """

    def __init__(self,image_file_path,pos=pygame.Rect(0,0,0,0)):
        self.xvel = self.yvel= 1
        self.pos = pos
        self.image = pygame.image.load(image_file_path).convert_alpha()

    def move(self):
        """ Implement your own movement """

    def draw(self,screen):
        self.move()
        screen.blit(self.image,self.pos)