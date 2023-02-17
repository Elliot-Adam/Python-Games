import pygame
import random
import math
import time
pygame.init()

def start():
    global playerX,playerY,dir,score,alone,speed,playerWidth,playerHeight,game_over,tailList
    tailList = []
    game_over = False
    playerX,playerY = SCREEN_LENGTH / 2 - 1, SCREEN_HEIGHT / 2 - 1    
    fruitRepos()
    dir = 'STOP'
    score = 0
    alone = True
    speed = 10
    playerHeight = 10
    playerWidth = 10

def logic():
    global score,alone,speed,tailList,playerY,playerX,game_over
    for rect in tailList:
        if rect.x == playerX and rect.y == playerY:
            game_over = True


    if distance(playerX,playerY,fruitX,fruitY) < playerWidth + 2:
        fruitRepos()
        score += 1
        if alone:
            alone = False
        tailList.append(pygame.Rect(playerX,playerY,playerWidth - 1,playerHeight - 1))

    updateTail()
    match dir:
        case 'UP':
            playerY -= speed
        case 'DOWN':
            playerY += speed
        case 'LEFT':
            playerX -= speed
        case 'RIGHT':
            playerX += speed

    if playerX <= 15 or playerX + playerWidth >= SCREEN_LENGTH - 15 or playerY <= 15 or playerY + playerHeight >= SCREEN_HEIGHT - 15:
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

def PlayerInput():
    global dir,isRunning,game_over
    keys = pygame.key.get_pressed()
    if not game_over:
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and (dir != 'DOWN' or alone):
            dir = 'UP'
            return

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (dir != 'UP' or alone):
            dir = 'DOWN'
            return

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (dir != 'RIGHT' or alone):
            dir = 'LEFT'
            return

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (dir != 'LEFT' or alone):
            dir = 'RIGHT'
            return
            
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
        for num,tail in enumerate(tailList):
            colorVal = 225 + len(tailList) - num
            pygame.draw.rect(SCREEN,(0,0,colorVal),tail)
        
    
    else:
        message = ['Q or X to quit' ,'R or J to continue','Final Score: {}'.format(score)]
        for num,line in enumerate(message):
            regFont = pygame.font.Font(None,30)
            ascoreprint = regFont.render(line,True,(255,255,255))
            ascore_rect = ascoreprint.get_rect(center = (SCREEN_LENGTH/2,SCREEN_HEIGHT/2 - 50 + num * 50))
            SCREEN.blit(ascoreprint,ascore_rect)
    
def distance(x1,y1,x2,y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2) **2)

def updateTail():
    
    global tailList,playerX,playerY
    if len(tailList):
        prevX = tailList[0].x
        prevY = tailList[0].y
        tailList[0].x = playerX
        tailList[0].y = playerY
        for rect in tailList[1:]:
            prev2X = rect.x
            prev2Y = rect.y
            rect.x = prevX
            rect.y = prevY
            prevX = prev2X
            prevY = prev2Y

def fruitRepos():
    global fruitX,fruitY
    edgeX = SCREEN_LENGTH - 30
    edgeY = SCREEN_HEIGHT - 30
    fruitX,fruitY = random.choice(range(15,edgeX)),random.choice(range(15,edgeY))

if __name__ == '__main__':
    CLOCK = pygame.time.Clock()
    FPS = 20

    SCREEN_LENGTH = 500
    SCREEN_HEIGHT = 500
    name = 'Snake'
    icon = pygame.image.load('Snake.png')

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
    pygame.display.set_caption(name)
    pygame.display.set_icon(icon)
    isRunning = True
    start()
    while isRunning:
        PlayerInput()
        logic()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()