from screen import Screen
from button import Button
from settings import *
import threading
import pygame
pygame.init()

class Positions:
    def set_new(self,height : int):
        self.UPPER = height - 2 * SIZE
        self.LOWER = self.UPPER + SIZE

    def set_up(self):
        self.set_new(HEIGHT)

class Colors:
    color_dict = pygame.colordict.THECOLORS
    white : pygame.Color = color_dict['white']
    navy : pygame.Color = color_dict['navy']
    black : pygame.Color = (0,0,0,255)
    color : pygame.Color = white

class Utility:
    def getSpecialButtons(screen : Screen,positions : Positions) -> list[Button]:
        """Returns a list of [resetButton,eraserButton]"""
        resetRect = pygame.Rect(screen.SCREEN.get_width() - 2 * SIZE, positions.UPPER,SIZE,SIZE)
        eraserRect = pygame.Rect(screen.SCREEN.get_width() - 2 * SIZE,positions.LOWER,SIZE,SIZE)

        resetImg = pygame.image.load('Paint/Assets/reset.png')
        eraserImg = pygame.image.load('Paint/Assets/eraser.png')
        
        resetButton = Button(resetRect,None,pygame.transform.scale(resetImg,DIMS))
        eraserButton = Button(eraserRect,None,pygame.transform.scale(eraserImg,DIMS))
        return [resetButton,eraserButton]

    def getSizeButtons(screen : Screen,positions : Positions) -> list[Button]:
        upRect = pygame.Rect(screen.SCREEN.get_width() - SIZE, positions.UPPER,SIZE,SIZE)
        downRect = pygame.Rect(screen.SCREEN.get_width() - SIZE,positions.LOWER,SIZE,SIZE)

        upImg = pygame.image.load('Paint/Assets/plus.png')
        downImg = pygame.image.load('Paint/Assets/minus.png')
        
        upButton = Button(upRect,None,pygame.transform.scale(upImg,(SIZE,SIZE)))
        downButton = Button(downRect,None,pygame.transform.scale(downImg,(SIZE,SIZE)))
        return [upButton,downButton]

    def getAllUniqueButtons(screen : Screen, positions : Positions):
        buttons = []
        #Appending the reset and eraser buttons
        resetButton,eraserButton = Utility.getSpecialButtons(screen,positions)
        
        resetButton.display(screen)
        eraserButton.display(screen)
        buttons.append((resetButton,IDS['RESET']))
        buttons.append((eraserButton,IDS['ERASE']))

        #Appending size changer buttons
        upButton,downButton = Utility.getSizeButtons(screen,positions)

        upButton.display(screen)
        downButton.display(screen)    
        buttons.append((upButton,IDS['SIZE_UP']))
        buttons.append((downButton,IDS['SIZE_DOWN']))
        return buttons

    def buttonMaker(coords : tuple[int,int], size : tuple[int,int], color : tuple[int,int,int], screen : Screen) -> Button:
        rect = pygame.Rect((coords[0],coords[1],size[0],size[1]))
        pygame.draw.rect(screen.SCREEN,color,rect)
        pygame.draw.rect(screen.SCREEN,Colors.black,rect,SIZE // BORDER_CONSTANT)
        button = Button(rect,None)
        return button,color
    
def button_setup(screen : Screen, positions : Positions) -> list[Button,tuple[int,int,int]]:
    buttons = []
    #Appending each color to the button menu drawing the buttons as well
    name_set = set()

    order = []
    for k, v in pygame.colordict.THECOLORS.items():
        total = v[0] + v[1] + v[2]
        if total < 180 or total > 700:
            continue
        
        trimmed = k.translate(str.maketrans('1234567890','          ')).strip()
        if trimmed not in name_set:
            #print(trimmed)
            name_set.add(trimmed)
            order.append(v)

    placement = {0 : positions.UPPER, 1 : positions.LOWER}
    for index, color in enumerate(order):
        if SIZE * (index // 2 + 3) > screen.SCREEN.get_width():
            break
        
        x = SIZE * (index // 2)
        y = placement[index % 2]
        buttons.append(Utility.buttonMaker((x,y),DIMS,color,screen))

    buttons.extend(Utility.getAllUniqueButtons(screen,positions))
    
    return buttons

def paint(screen : Screen, position : tuple[int,int], RADIUS : int, color : tuple[int,int,int]):
    pygame.draw.rect(screen.SCREEN,color, (position[0] - RADIUS,position[1] - RADIUS,RADIUS * 2, RADIUS * 2))

def refresh_size_monitor(screen : Screen):
    rect = pygame.Rect(0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE)
    pygame.draw.rect(screen.SCREEN,Colors.black,rect)

def button_decode(screen : Screen, buttons : list, colorObj : Colors, position : tuple, radius : int):
    for buttonZip in buttons:
        button : Button = buttonZip[0]
        color = buttonZip[1]
        if button.point_in_rect(position):
            #If color in ids, it is a special button and not one of the color options
            og_radius = radius
            if color in IDS.values():
                if color == IDS['RESET']:
                    pygame.draw.rect(screen.SCREEN,(0,0,0),pygame.Rect(0,0,screen.SCREEN.get_width(),screen.SCREEN.get_height() - 2 * SIZE))
                    color = colorObj.color

                if color == IDS['ERASE']:
                    color = Colors.black

                if color == IDS['SIZE_UP']:
                    if radius + SIZE_CHANGE <= SIZE_MAX:
                        radius += SIZE_CHANGE
                    color = colorObj.color
                        
                if color == IDS['SIZE_DOWN']:
                    if radius - SIZE_CHANGE >= SIZE_MIN:
                        radius -= SIZE_CHANGE
                    color = colorObj.color

            if colorObj.color != color:
                #print(f'Changed from {colorObj.color} to {color}')
                colorObj.color = color

            if radius != og_radius:
                refresh_size_monitor(screen)

    return radius

def run():
    screen = Screen(HEIGHT,WIDTH,'Paint','Paint/Assets/logo.png',resizable=True)
    screen.start_up()
    radius = CURSOR_SIZE
    colorObj = Colors()
    positions = Positions()
    positions.set_up()

    isRunning = True
    buttons = button_setup(screen,positions)
    while isRunning:
        position = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and position[1] < screen.SCREEN.get_height() - 2 * SIZE - radius:
            paint(screen,position,radius,colorObj.color)

        #Seperator rect 
        pygame.draw.rect(screen.SCREEN,Colors.navy,pygame.Rect(0,positions.UPPER,screen.SCREEN.get_width(),SIZE // BORDER_CONSTANT))

        #pygame.draw.rect(screen.SCREEN,Colors.black,pygame.Rect(0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE))
        regFont = pygame.font.Font(None,SMALL_BUTTON_SIZE)
        rendered = regFont.render(str(radius),True,Colors.white,Colors.black)
        rendered_rect = rendered.get_rect(center = (SMALL_BUTTON_SIZE / 2,SMALL_BUTTON_SIZE * 3/2))
        #rendered_rect = pygame.Rect(0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE)
        screen.SCREEN.blit(rendered,rendered_rect)

        pygame.draw.rect(screen.SCREEN,colorObj.color,pygame.Rect(0,0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE))
        pygame.draw.rect(screen.SCREEN,Colors.black,pygame.Rect(0,0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE),SMALL_BUTTON_SIZE // BORDER_CONSTANT)

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                positions.set_new(screen.SCREEN.get_height())
                buttons = button_setup(screen,positions)

            if event.type == pygame.MOUSEBUTTONDOWN:
                radius = button_decode(screen,buttons,colorObj,position,radius)

            if event.type == pygame.QUIT:
                isRunning = False

        pygame.display.update()

if __name__ == '__main__':
    run()