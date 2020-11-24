import pygame

class Render():

    game_objecs = []

    def __init__(self,screen):
        self.screen = screen
    
    def register_object(self,*objs):
        for obj in objs:
            self.game_objecs.append(obj)

    def destroy_object(self,obj):
        self.game_objecs.remove(obj)

    def destroy_all_objects(self):
        for i in self.game_objecs:
            del i

    def draw_objects(self):
        for obj in self.game_objecs:
            obj.draw(self.screen)