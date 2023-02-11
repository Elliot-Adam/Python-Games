import pygame
import random
import math
pygame.init()

def start():
    global playerX,playerY,dir,score,tailLen,speed,playerWidth,playerHeight,game_over
    game_over = False
    playerX,playerY = SCREEN_LENGTH / 2 - 1, SCREEN_HEIGHT / 2 - 1    
    fruitRepos()
    dir = 'STOP'
    score = 0
    tailLen = 0
    speed = 10
    playerHeight = 10
    playerWidth = 10

def logic():
    global score,tailLen,playerY,playerX,game_over
    if distance() < playerWidth + 2:
        fruitRepos()
        score += 1
        tailLen += 1

    match dir:
        case 'UP':
            playerY -= speed
        case 'DOWN':
            playerY += speed
        case 'LEFT':
            playerX -= speed
        case 'RIGHT':
            playerX += speed

    if playerX <= 5 or playerX + playerWidth >= SCREEN_LENGTH - 15 or playerY <= 5 or playerY + playerHeight >= SCREEN_HEIGHT - 15:
        #Changes values so player can see snake after runs into wall
        if playerX == -1:
            playerX += 1
        
        if playerX == SCREEN_LENGTH:
            playerX -= 1
        
        if playerY == -1: 
            playerY += 1
        
        if playerY == SCREEN_HEIGHT:
            playerY -= 1
    
        
        game_over = True

def input():
    global dir,isRunning,game_over
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_w] or keys[pygame.K_UP] and (dir != 'DOWN' or not tailLen):
            dir = 'UP'

        if keys[pygame.K_s] or keys[pygame.K_DOWN] and (dir != 'UP' or not tailLen):
            dir = 'DOWN'

        if keys[pygame.K_a] or keys[pygame.K_LEFT] and (dir != 'RIGHT' or not tailLen):
            dir = 'LEFT'

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and (dir != 'LEFT' or not tailLen):
            dir = 'RIGHT'
    else:
        if keys[pygame.K_q] or keys[pygame.K_x]:
            isRunning = False
        if keys[pygame.K_r] or keys[pygame.K_j]:
            start()

def draw():
    SCREEN.fill((0,0,0))
    if not game_over:
        borderWidth = 9
        rectX = 5
        rectY = 5
        rectWidth = SCREEN_LENGTH - 10
        rectHeight = SCREEN_HEIGHT - 10
        #Score
        regFont = pygame.font.Font(None,300)
        ascoreprint = regFont.render(str(score),True,(255,255,255))
        ascore_rect = ascoreprint.get_rect(center = (SCREEN_LENGTH/2,SCREEN_HEIGHT/2))
        SCREEN.blit(ascoreprint,ascore_rect)
        #Walls
        pygame.draw.rect(SCREEN, (255, 255, 255), (rectX, rectY, rectWidth, rectHeight),borderWidth) 
        #Snake
        pygame.draw.rect(SCREEN,(0,100,255),(playerX,playerY,playerWidth,playerHeight))
        #Fruit
        pygame.draw.rect(SCREEN,(255,0,0),(fruitX,fruitY,playerWidth - 2,playerHeight - 2))
    
    else:
        message = ['Q or X to quit' ,'R or J to continue']
        for num,line in enumerate(message):
            regFont = pygame.font.Font(None,30)
            ascoreprint = regFont.render(line,True,(255,255,255))
            ascore_rect = ascoreprint.get_rect(center = (SCREEN_LENGTH/2,SCREEN_HEIGHT/2 - 50 + num * 50))
            SCREEN.blit(ascoreprint,ascore_rect)
    
def distance():
    return math.sqrt((playerX - fruitX)**2 + (playerY - fruitY) **2)

def fruitRepos():
    global fruitX,fruitY
    edgeX = SCREEN_LENGTH - 15
    edgeY = SCREEN_HEIGHT - 15
    fruitX,fruitY = random.choice(range(15,edgeX)),random.choice(range(15,edgeY))

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 20

    SCREEN_LENGTH = 500
    SCREEN_HEIGHT = 500
    name = 'Snake'
    icon = pygame.image.load('c:/Users/Elliot/Specific Projects/Python-Games/Snake.png')

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    isRunning = True
    start()
    while isRunning:
        input()
        logic()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()