#Imports
import pygame
import math
import random
pygame.init()

#Classes
class Ball:
    def __init__(self,x,y,vx,vy,radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.incrementSpeed = False
        self.accy = 0.3
        self.accx = 0.3
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def direct_distance(self,other):
        return math.sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))
class Paddle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def paddle_move(self, keyup,keydown):
        allKeys = pygame.key.get_pressed()
        if allKeys[keyup]:
            if self.y - 7 >= 0:
                self.y -= 7
            else:
                self.y += 5
        if allKeys[keydown]:
            if self.y + self.height + 7 <= displayHeight:
                self.y += 7
            else:
                self.y -= 5
    def move(self):
        if self.x == 10:
            self.paddle_move(pygame.K_w,pygame.K_s)   
        else:
            self.paddle_move(pygame.K_UP,pygame.K_DOWN)

#Function Defs
def score_update(ascore,bscore):
    regFont = pygame.font.Font(None,40)
    ascoreprint = regFont.render(str(ascore),True,white)
    ascore_rect = ascoreprint.get_rect(center = (displayWidth/3,displayHeight/5))
    bscoreprint = regFont.render(str(bscore),True,white)
    bscore_rect = bscoreprint.get_rect(center = (displayWidth*(2/3),displayHeight/5))
    SCREEN.blit(ascoreprint,ascore_rect)
    SCREEN.blit(bscoreprint,bscore_rect)
def hit_paddle(ball,paddle):
    #Check hit corner top right
    if math.sqrt((ball.x - paddle.x + paddle.width)**2 + (ball.y - paddle.y)**2) < ball.radius:
        ball.vy *= -1 
            
        return True
    #Check hit corner bottom right
    if math.sqrt((ball.x - paddle.x + paddle.width)**2 + (ball.y - paddle.y - paddle.height)**2) < ball.radius:
        ball.vy *= -1 
        return True
    #Check hit
    if ball.vx < 0:
        if ball.x - ball.radius <= paddle.x + paddle.width + 2 and ball.y > paddle.y and ball.y < paddle.y + paddle.height:
            return True
    else:
        if ball.x + ball.radius >= paddle.x - paddle.width - 2 and ball.y > paddle.y and ball.y < paddle.y + paddle.height:
            return True
    return False
def hit_sides(y,dh,radius):
    if (y < radius) or y > (dh - radius):
        return True
def hit_front(ball):
    if ball.x < ball.radius:
        return True
    return False
def hit_back(ball):
    if ball.x + ball.radius > displayWidth:
        return True
    return False
def reset(SINGLEball):
    SINGLEball.x = displayWidth/2
    SINGLEball.y = random.randint(10,displayHeight - 10)
    if random.randint(0,2) % 2 == 0:
        ball.vy *= -1
def gmode(mode):
    global ball
    global paddle_a
    global paddle_b
    global ball1
    global ball2
    global speed
    paddle_a = Paddle(10,displayHeight/2,3,40)
    paddle_b = Paddle(490,displayHeight/2,3,40)
    if mode == 1:
        speed = 30
        ball = Ball(displayWidth/2,displayHeight/2,10,10,10)
    if mode == 2:
        speed = 30
        ball1 = Ball(displayWidth/2,(3*displayHeight/5),6,6,10)
        ball2 = Ball(displayWidth/2,(2*displayHeight/5),-6,-6,10)
    if mode == 3:
        speed = 45
        ball = Ball(displayWidth/2,displayHeight/2,6,6,20)
        paddle_a.height = 20
        paddle_b.height = 20 
    if mode == 4:
        speed = 35
        ball = Ball(displayWidth/2,displayHeight/2,6,6,10)
        ball.incrementSpeed = True
def gmode_getter():
    messageprint = []
    pygame.time.set_timer(pygame.USEREVENT,10000)
    timer_active = True
    regFont = pygame.font.Font(None,30)
    message = ['Input' ,'1. Normal ','2. Multiball ','3. Big Ball, Small Paddle','4.Speed Pong']
    for text in message:
        messageprint.append(regFont.render(text,True,white))
    for line in range(len(messageprint)):
        print(line)
        message_rect = messageprint[line].get_rect(center = (displayWidth/2,displayHeight/5 + 50*line))
        SCREEN.blit(messageprint[line],message_rect)
    pygame.display.flip()
    while timer_active:
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                timer_active = False
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                    print(event.key,pygame.K_1,pygame.K_2,pygame.K_3)
                    timer_active = False
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2
                if event.key == pygame.K_3:
                    return 3
                if event.key == pygame.K_4:
                    return 4
def ballCrash(ballUno,ballDos):
    if ballUno.direct_distance(ballDos) < ballUno.radius*2:
        return True
    

#Variable Defs
clock = pygame.time.Clock()
speed = 20
displayWidth = 500
displayHeight = 300
ascore = 0
bscore = 0
SCREEN = pygame.display.set_mode((displayWidth,displayHeight))
black = (0,0,0)
white = (255,255,255)
gameIcon = pygame.image.load('Pong_Image.png')
pygame.display.set_caption("Pong")
pygame.display.set_icon(gameIcon)
mode = gmode_getter()
gmode(mode)
#Game Loop
if __name__ == "__main__":
    while True:
        if mode == 1 or mode == 3 or mode == 4:
            clock.tick(speed)
            pygame.draw.rect(SCREEN,white,(paddle_a.x,paddle_a.y,paddle_a.width,paddle_a.height))
            pygame.draw.rect(SCREEN,white,(paddle_b.x,paddle_b.y,paddle_b.width,paddle_b.height))
            pygame.draw.circle(SCREEN,white,(ball.x,ball.y),ball.radius)
            ball.move()
            paddle_a.move()
            paddle_b.move()
            if hit_front(ball):
                bscore += 1
                reset(ball)
            if hit_back(ball):
                ascore += 1
                reset(ball)
            if hit_paddle(ball,paddle_a):
                if ball.incrementSpeed:
                    if ball.vy < 0:
                        ball.vy -= ball.accy
                        ball.accy -= 0.005
                        ball.vx -= ball.accx
                        ball.accx -= 0.005
                    if ball.vy > 0:
                        ball.vy += ball.accy
                        ball.accy += 0.005
                        ball.vx += ball.accx
                        ball.accx -= 0.005
                ball.vx = abs(ball.vx) 
            if hit_paddle(ball,paddle_b):
                ball.vx = abs(ball.vx) * -1
            if hit_sides(ball.y,displayHeight,ball.radius):
                ball.vy *= -1
            score_update(ascore,bscore)
            pygame.display.update()
        if mode == 2:
            clock.tick(speed)
            pygame.draw.rect(SCREEN,white,(paddle_a.x,paddle_a.y,paddle_a.width,paddle_a.height))
            pygame.draw.rect(SCREEN,white,(paddle_b.x,paddle_b.y,paddle_b.width,paddle_b.height))
            pygame.draw.circle(SCREEN,white,(ball1.x,ball1.y),ball1.radius)
            pygame.draw.circle(SCREEN,white,(ball2.x,ball2.y),ball2.radius)
            ball1.move()
            ball2.move()
            paddle_a.move()
            paddle_b.move()
            for ball in [ball1,ball2]:
                if hit_front(ball):
                    bscore += 1
                    reset(ball)
                if hit_back(ball):
                    ascore += 1
                    reset(ball)
                if ballCrash(ball1,ball2):
                    ball1.vx *= -1
                    ball2.vx *= -1
                    ball1.vy *= -1
                    ball2.vy *= -1
                if hit_paddle(ball,paddle_a):
                    ball.vx = abs(ball.vx) 
                if hit_paddle(ball,paddle_b):
                    ball.vx = abs(ball.vx) * -1
                if hit_sides(ball.y,displayHeight,ball.radius):
                    ball.vy *= -1
            score_update(ascore,bscore)
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.fill(black)