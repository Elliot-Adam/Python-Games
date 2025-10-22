import pygame
import _thread
import time
from screen import Screen
pygame.init()

class Move:
    def __init__(self,direction : str,position : str) -> None:
        self.direction = direction # LEFT RIGHT UP OR DOWN, Direction of move
        self.position = position # ATTACK or DEFEND, which person is doing what

class Player:
    def __init__(self,position : str, coord : tuple) -> None:
        self.position = position
        self.coord = coord
        
    hits = 0
    hit_list = []
    move : Move = None

    def input(self) -> Move:
        allkeys = pygame.key.get_pressed()
        if allkeys[pygame.K_w] or allkeys[pygame.K_UP]:
            return Move('UP', self.position)
        if allkeys[pygame.K_s] or allkeys[pygame.K_DOWN]:
            return Move('DOWN', self.position)
        if allkeys[pygame.K_a] or allkeys[pygame.K_LEFT]:
            return Move('LEFT', self.position)
        if allkeys[pygame.K_d] or allkeys[pygame.K_RIGHT]:
            return Move('RIGHT', self.position)

    def hit_incr(self):
        self.hits += 1

    def hit_list_clear(self):
        self.hit_list.clear()

    def switch_position(self):
        switch = {0:'ATTACK',1:'DEFEND'}
        for i in range(1):
            if self.position == switch[i]:
                self.position = switch[1-i]

def ending(celly_direction):
    #TODO
    pass

def turn(player1 : Player, player2 : Player):
    assert player1.move.position == 'ATTACK'
    assert player2.move.position == 'DEFEND'

    _thread.start_new_thread(player1.input,())
    _thread.start_new_thread(player2.input,())
    regFont = pygame.font.Font(None,300)
    countdown = 3
    for i in range(3):
        x = i + 1
        timeprint = regFont.render(str(x),True,(255,255,255))
        time_rect = timeprint.get_rect(center = ())
        SCREEN.blit(ascoreprint,ascore_rect)

    if player1.move.direction == player2.move.direction:
        player1.hit_incr()
        if player1.hits == 3:
            ending(player1.move.position)

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
str.strip()