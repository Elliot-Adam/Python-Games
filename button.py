import pygame

class Button:
    def __init__(self,rect : pygame.Rect, func : function):
        self.rect = rect
        self.func = func
        #Should be ran from _thread.start_new_thread

    def run(self,params):
        if pygame.mouse.get_pos() in self.rect:
            self.func(params)