import pygame
import copy
import random

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

    def pillarDeath(self):
        self.vel = 0
        self.accel = 0
    
class Pillar:
    move_speed = 3
    width = 100
    #height = 200
    def __init__(self,x,y,upsideDown : bool) -> None:
        self.x = x
        self.y = y
        self.upsideDown = upsideDown
        self.height = self.y
        if self.upsideDown:
            self.scoreValid = True
            self.y = 0
        else:
            self.scoreValid = False
            self.height = SCREEN_HEIGHT - self.y
        self.rect : pygame.Rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def move(self):
        self.x -= self.move_speed
        self.rect.x -= self.move_speed

    def collisDetect(self,bird : Bird) -> bool:
        if self.upsideDown:
            yoffset = 5
        else:
            yoffset = 15
        xoffset = 10
        woffset = 20
        hoffset = 20
        pillarHitx = self.rect.x + xoffset
        pillarHity = self.rect.y + yoffset
        newRect = pygame.Rect(pillarHitx,pillarHity,self.width - woffset ,self.height - hoffset )
        if newRect.colliderect(bird.rect):
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
    
    bird_img = Bird.img
    pipe_img = pygame.image.load('flappy_bird/pipe.png')
    scaled_bird = pygame.transform.scale(bird_img,(Bird.width,Bird.height))
    SCREEN.blit(scaled_bird,(bird.x,bird.y))
    for pillar in pillarList:
        scaled_pipe = pygame.transform.scale(pipe_img,(pillar.width,pillar.height))
        if pillar.upsideDown:
            new_pipe_img = pygame.transform.flip(scaled_pipe, False, True)
        else:
            new_pipe_img = scaled_pipe
        SCREEN.blit(new_pipe_img,(pillar.x,pillar.y))
        #Debugging mode
        #pygame.draw.rect(SCREEN,(255,255,255),pillar.rect)
        #Hitbox debugging
        #if pillar.upsideDown:
        #    yoffset = 5
        #else:
        #    yoffset = 15
        #xoffset = 10
        #woffset = 20
        #hoffset = 20
        #pillarHitx = pillar.rect.x + xoffset
        #pillarHity = pillar.rect.y + yoffset
        #newRect = pygame.Rect(pillarHitx,pillarHity,Pillar.width - woffset ,Pillar.height - hoffset )
        #pygame.draw.rect(SCREEN,(255,255,255),newRect)
#
    ##Bird hitbox debugging 
    #pygame.draw.rect(SCREEN,(255,0,0),bird.rect)
    regFont = pygame.font.Font(None,75)
    scoremsg = regFont.render(str(score),True,(0,0,0))
    score_rect = scoremsg.get_rect(center = (SCREEN_WIDTH/2,50))
    SCREEN.blit(scoremsg,score_rect)

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

def logic(timer):
    global gameOver,pillarList,score
    if timer % 100  == 0:
        topHeight = 50
        distance = 125
        ycoord = random.randint(topHeight,SCREEN_HEIGHT - topHeight - distance)
        topCol = Pillar(SCREEN_WIDTH,ycoord,True)
        botCol = Pillar(SCREEN_WIDTH,ycoord + distance,False)
        pillarList.append(topCol)
        pillarList.append(botCol)

    #Logic for flapping
    bird.vel += bird.accel
    bird.y += bird.vel
    bird.rect.y += bird.vel
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

    #Moving pillars
    if not gameOver:
        for pillar in pillarList:
            pillar.move()

    #Logic for dying on pillars
    for pillar in pillarList:
        if pillar.collisDetect(bird):
            gameOver = True
            bird.pillarDeath()

        if (bird.x + bird.width) in range(int(pillar.x + pillar.width / 4),int(pillar.x + (3 * pillar.width / 4))) and pillar.scoreValid:
            score += 1
            pillar.scoreValid = False

def input():
    global pressed,isRunning,gameOver
    key = pygame.key.get_pressed()
    if not gameOver:
        if (key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and not pressed:
            bird.flap()
            pressed = True
    else:
        if key[pygame.K_q] or key[pygame.K_x]:
            isRunning = False

        if key[pygame.K_r] or key[pygame.K_j]:
            gameOver = False
            start()

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
    timer = 0

    start()
    while isRunning:
        draw()
        logic(timer)
        input()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                pressed = False

            if event.type == pygame.QUIT:
                isRunning = False
            
        timer += 1
        CLOCK.tick(FPS)
        pygame.display.update()

    pygame.quit()