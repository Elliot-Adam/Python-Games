import pygame

class Button:
    def __init__(self,rect : pygame.Rect, func):
        self.rect = rect
        self.func = func
        #Should be ran from _thread.start_new_thread(button.run) or threading.Thread(target=button.run).start()

    def point_in_rect(self,point : tuple) -> bool:
        x = point[0]
        y = point[1]
        if not (self.rect.left <= x <= self.rect.right):
            return False
        if not (self.rect.top <= y <= self.rect.bottom):
            return False
        return True

    def run(self,*params):
        self.func(params)

        