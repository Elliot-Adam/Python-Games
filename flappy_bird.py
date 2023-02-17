import pygame
import copy

pygame.init()

gravity = 1

class Bird:
    boost = -2
    width = 50
    height = 50
    accel = copy.copy(gravity)
    vel = 0
    flapping = False
    flappingTimer = 0
    flappingMax = 5
    img = pygame.image.load('flappy_bird/bird.png')

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect : pygame.Rect = pygame.Rect(self.x,self.y,self.width,self.height)
    
    def flap(self):
        self.vel = 0
        self.accel = self.boost
        self.flapping = True

    def nonPillarDeath(self):
        self.img = pygame.transform.flip(self.img,False,True)
        self.vel = 0
        self.accel = copy.copy(gravity)
    


class Pillar:
    move_speed = 3
    width = 10
    height = 50
    def __init__(self,x,y,upsideDown : bool) -> None:
        self.x = x
        self.y = y
        self.upsideDown = upsideDown
        self.rect : pygame.Rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def move(self):
        self.x -= self.move_speed

    def collisDetect(self,bird : Bird) -> bool:
        if self.rect.colliderect(bird.rect):
            return True
        return False

def start():
    global bird,pillarList,pressed, gameOver,score
    pillarList = []
    xoffset = 45
    yoffset = 100
    bird = Bird(SCREEN_WIDTH / 2 - xoffset ,SCREEN_HEIGHT / 2 - yoffset)
    pressed = False
    gameOver = False
    score = 0

def draw():
    drawBg()
    regFont = pygame.font.Font(None,75)
    scoremsg = regFont.render(str(score),True,(0,0,0))
    score_rect = scoremsg.get_rect(center = (SCREEN_WIDTH/2,100))
    SCREEN.blit(scoremsg,score_rect)
    bird_img = Bird.img
    pipe_img = pygame.image.load('flappy_bird/pipe.png')
    scaled_bird = pygame.transform.scale(bird_img,(Bird.width,Bird.height))
    scaled_pipe = pygame.transform.scale(pipe_img,(Pillar.width,Pillar.height))
    SCREEN.blit(scaled_bird,(bird.x,bird.y))
    for pillar in pillarList:
        if pillar.upsideDown:
            new_pipe_img = pygame.transform.flip(scaled_pipe, False, True)
        else:
            new_pipe_img = scaled_pipe
        SCREEN.blit(new_pipe_img,(pillar.x,pillar.y))
        
    if gameOver:
        message = ['Q or X to quit' ,'R or J to continue','Final Score: {}'.format(score)]
        for num,line in enumerate(message):
            regFont = pygame.font.Font(None,30)
            scoreprint = regFont.render(line,True,(255,255,255))
            score_rect = scoreprint.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 50 + num * 50))
            SCREEN.blit(scoreprint,score_rect)

def drawBg():
    bg = pygame.image.load('flappy_bird/bg.png')
    scaled_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
    SCREEN.blit(scaled_bg,(0,0))

def logic():
    global gameOver
    #Logic for flapping
    bird.vel += bird.accel
    bird.y += bird.vel
    if bird.flapping:
        bird.flappingTimer += 1
    
        if bird.flappingTimer == bird.flappingMax:
            bird.accel = copy.copy(gravity)
            bird.flapping = False
            bird.flappingTimer = 0

    #Logic for dying by hitting the ground or ceiling
    if bird.y < 0:
        gameOver = True
        bird.nonPillarDeath()

    if (bird.y + Bird.height) + 12 >= SCREEN_HEIGHT:
        gameOver = True
        bird.nonPillarDeath()   
        bird.accel = 0

def input():
    global pressed
    key = pygame.key.get_pressed()
    if (key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and not pressed:
        bird.flap()
        pressed = True

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 20

    SCREEN_HEIGHT = 525
    SCREEN_WIDTH = 300
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    icon = pygame.image.load('flappy_bird/bird.png')
    name = 'Flappy Bird'

    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    
    isRunning = True

    start()
    while isRunning:
        draw()
        logic()
        if not gameOver:
            input()
        print(pygame.mouse.get_pressed()[0])
        for event in pygame.event.get():
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                pressed = False

            if event.type == pygame.QUIT:
                isRunning = False
            
        CLOCK.tick(FPS)
        pygame.display.update()

    pygame.quit()