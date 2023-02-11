import pygame
pygame.init()

def draw():
    bg = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/ChessBoard.png')
    SCREEN.blit(bg,(0,0))
class Board:
    def setBoard():
        pass
class Piece:   
    pass

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 20

    SCREEN_LENGTH = 750
    SCREEN_HEIGHT = 750
    name = 'Chess'
    icon = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Chess/WHITE_PAWN.png')

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()

    pygame.quit()