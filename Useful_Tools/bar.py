import pygame

class Bar:
    def __init__(self,total):
        self.total = total
        self.current = 0
        self.valid = True

    def __add__(self,other : int):
        if self.valid and self.current <= self.total:
            print(f'{other} added to {self.current} to make {other + self.current}')
            self.current += other
            self.valid = False

    def display_bar(self,screen):
        pygame.display.get_window_size()
        if self.current != 0:
            ratio = self.current / self.total
            bar_progress = int(ratio * pygame.display.get_window_size()[0])
            pygame.draw.rect(screen.SCREEN,(0,255,0),pygame.Rect(0,400,bar_progress,pygame.display.get_window_size()[1] - 400))