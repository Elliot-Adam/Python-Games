import pygame

class Bird:
    boost = 5
    width = 5
    height = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect : pygame.Rect = pygame.Rect(self.x,self.y,self.width,self.height)
    
    def flap(self):
        self.y -= self.boost

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
    global bird,pillarList
    pillarList = []
    bird = Bird(0,0)

def draw():
    drawBg()
    bird_img = pygame.image.load('flappy_bird/bird.png')
    pillar_mid_img = pygame.image.load('flappy_bird/pipe_mid.png')
    pillar_top_img = pygame.image.load('')
    scaled_bird = pygame.transform.scale(bird_img,(Bird.width,Bird.height))
    SCREEN.blit(scaled_bird,(bird.x,bird.y))
    for pillar in pillarList:
        SCREEN.blit()


def drawBg():
    bg = pygame.image.load('flappy_bird/bg.png')
    scaled_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
    SCREEN.blit(scaled_bg,(0,0))

def logic():
    pass

def input():
    pass



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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        CLOCK.tick(FPS)
        pygame.display.update()

    pygame.quit()