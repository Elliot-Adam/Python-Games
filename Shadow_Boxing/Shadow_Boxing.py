import pygame
import _thread
import time
from screen import Screen
pygame.init()

class Move:
    def __init__(self,direction : str,position : str = None) -> None:
        self.direction = direction # LEFT RIGHT UP OR DOWN, Direction of move
        self.position = position # ATTACK or DEFEND, which person is doing what

    def __eq__(self, other):
        assert isinstance(other,Move)
        assert self.position == 'ATTACK'
        if self.direction == other.direction:
            return True
        return False

class Player:
    def __init__(self,position, input_dict : dict[int,Move]) -> None:
        self.position = position
        self.inp_list = input_dict #gives the keys that correspond to which input, NOTE SHOULD BE PYGAME VALUES to move e.g. pygame.K_w for the w key to Move('UP',self.position)

    hits = 0
    hit_list = []
    move : Move = None

    def input(self,cd : int) -> Move:
        allkeys = pygame.key.get_pressed()
        for k,v in self.inp_list.items():
            if allkeys[k]:
                new_move = Move(v.direction, self.position)
                self.move = new_move
        time.sleep(cd)

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

def turn(player1 : Player, player2 : Player , screen : Screen):
    assert player1.move.position == 'ATTACK'
    assert player2.move.position == 'DEFEND'

    _thread.start_new_thread(player1.input,())
    _thread.start_new_thread(player2.input,())
    regFont = pygame.font.Font(None,300)
    countdown = 3
    for i in range(countdown):
        x = i + 1
        timeprint = regFont.render(str(x),True,(255,255,255))
        time_rect = timeprint.get_rect(center = (screen.SCREEN_WIDTH/2,screen.SCREEN_HEIGHT/2))
        screen.SCREEN.blit(timeprint,time_rect)
        time.sleep(1)

    if player1.move.direction == player2.move.direction:
        player1.hit_incr()
        if player1.hits == lives:
            ending(player1.move.position)

def draw(p1 : Player):
    pass

def run():
    screen = Screen(500,500,'Shadow Boxing')
    running = True
    game_clock = pygame.time.Clock()
    FPS = 30
    global lives
    lives = 3
    p1_inp_dict = {pygame.K_w : Move('UP'), pygame.K_s : Move('DOWN'), pygame.K_a : Move('LEFT'), pygame.K_d : Move('RIGHT')}
    p2_inp_dict = {pygame.K_UP : Move('UP'), pygame.K_DOWN : Move('DOWN'), pygame.K_LEFT : Move('LEFT'), pygame.K_RIGHT : Move('RIGHT')}
    p1 = Player('ATTACk',p1_inp_dict)
    p2 = Player('DEFEND',p2_inp_dict)
    while running:
        game_clock.tick(FPS)
        screen.start_up()
        turn(p1,p2,screen)
        time.sleep(1)
        turn(p2,p1,screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()