import pygame
from screen import Screen
pygame.init()

class Player:
    hits = 0
    def input(self):
        #Will return a Move object
        pass

class Move:
    def __init__(self,direction : str,position : str) -> None:
        self.direction = direction
        self.position = position

def run():
    screen = Screen(500,500,'Shadow Boxing')
    running = True
    game_clock = pygame.time.Clock()
    FPS = 30
    while running:
        game_clock.tick(FPS)
        screen.start_up()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()