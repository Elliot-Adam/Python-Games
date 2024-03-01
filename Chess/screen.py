import pygame

pygame.init()

class Screen:
    def __init__(self,height : int,width : int,name : str = None,icon : pygame.Surface = None ,bg : pygame.Surface = None):
        self.SCREEN_HEIGHT = height
        self.SCREEN_WIDTH = width
        self.name = name
        self.icon = icon
        self.bg =  bg
        self.start_up()

    def start_up(self):
        assert isinstance(self.SCREEN_HEIGHT,int) and isinstance(self.SCREEN_WIDTH,int)
        self.SCREEN = pygame.display.set_mode((self.SCREEN_HEIGHT,self.SCREEN_WIDTH))

        if self.bg:
            self.bg = pygame.image.load(self.bg).convert_alpha()
        if self.name:
            pygame.display.set_caption(self.name)
        if self.icon:
            self.icon = pygame.image.load(self.icon).convert_alpha()
            pygame.display.set_icon(self.icon)

    def draw_bg(self) -> None:
        scaled_bg = pygame.transform.scale(self.bg,(self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.SCREEN.blit(scaled_bg,(0,0))
