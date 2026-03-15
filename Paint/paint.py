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
    red : pygame.Color = color_dict['red1']
    blue : pygame.Color = color_dict['blue1']
    green : pygame.Color = color_dict['green1']
    yellow: pygame.Color = color_dict['yellow1']
    white : pygame.Color = color_dict['white']
    crimson : pygame.Color = color_dict['crimson']
    navy : pygame.Color = color_dict['navy']
    black : pygame.Color = (0,0,0,255)
    color : pygame.Color = white

def getSpecialButtons(screen : Screen,positions : Positions) -> list[Button]:
    """Returns a list of [resetButton,eraserButton]"""
    resetRect = pygame.Rect(screen.SCREEN.get_width() - SIZE, positions.UPPER,SIZE,SIZE)
    eraserRect = pygame.Rect(screen.SCREEN.get_width() - SIZE,positions.LOWER,SIZE,SIZE)

    resetImg = pygame.image.load('Paint/Assets/reset.png')
    eraserImg = pygame.image.load('Paint/Assets/eraser.png')
    
    resetButton = Button(resetRect,None,pygame.transform.scale(resetImg,DIMS))
    eraserButton = Button(eraserRect,None,pygame.transform.scale(eraserImg,DIMS))
    return [resetButton,eraserButton]

def getSizeButtons() -> list[Button]:
    #TODO
    pass

def color_selection_setup(screen : Screen, positions : Positions) -> list[Button,tuple[int,int,int]]:
    buttons = []
    #Appending each color to the button menu drawing the buttons as well
    order = [Colors.red,Colors.blue,Colors.green,Colors.yellow,Colors.crimson,Colors.navy,Colors.white]
    placement = {0 : positions.UPPER, 1 : positions.LOWER}
    for index, color in enumerate(order):
        if SIZE * (index + 1) > screen.SCREEN.get_width():
            break
        
        x = SIZE * (index // 2)
        y = placement[index % 2]
        buttons.append(buttonMaker((x,y),DIMS,color,screen))

    #Appending the reset and eraser buttons
    resetButton,eraserButton = getSpecialButtons(screen,positions)
    
    resetButton.display(screen)
    eraserButton.display(screen)
    buttons.append((resetButton,None))
    buttons.append((eraserButton,Colors.black))


    return buttons

def buttonMaker(coords : tuple[int,int], size : tuple[int,int], color : tuple[int,int,int], screen : Screen) -> Button:
    rect = pygame.Rect((coords[0],coords[1],size[0],size[1]))
    pygame.draw.rect(screen.SCREEN,color,rect)
    pygame.draw.rect(screen.SCREEN,Colors.black,rect,SIZE // BORDER_CONSTANT)
    button = Button(rect,None)
    return button,color

def paint(screen : Screen, position : tuple[int,int], RADIUS : int, color : tuple[int,int,int]):
    pygame.draw.rect(screen.SCREEN,color, (position[0] - RADIUS,position[1] - RADIUS,RADIUS * 2, RADIUS * 2))

def toolbar(screen : Screen, buttons : list, colorObj : Colors, position : tuple, left_click : bool):
    for buttonZip in buttons:
        button : Button = buttonZip[0]
        color = buttonZip[1]
        if button.point_in_rect(position) and left_click:
            if color == None:
                pygame.draw.rect(screen.SCREEN,(0,0,0),pygame.Rect(0,0,WIDTH,screen.SCREEN.get_height() - 2 * SIZE))
                color = Colors.white

            if colorObj.color != color:
                #print(f'Changed from {colorObj.color} to {color}')
                colorObj.color = color

def run():
    screen = Screen(HEIGHT,WIDTH,'Paint',resizable=True)
    screen.start_up()
    print(pygame.RESIZABLE * False)
    RADIUS = CURSOR_SIZE
    colorObj = Colors()
    positions = Positions()
    positions.set_up()
    print(screen.SCREEN.get_flags())

    isRunning = True
    buttons = color_selection_setup(screen,positions)
    while isRunning:
        position = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        toolbar(screen,buttons,colorObj,position,left_click)

        if left_click and position[1] < screen.SCREEN.get_height() - 2 * SIZE - RADIUS:
            paint(screen,position,RADIUS,colorObj.color)

        #Seperator rect 
        pygame.draw.rect(screen.SCREEN,Colors.navy,pygame.Rect(0,positions.UPPER,screen.SCREEN.get_width(),SIZE // BORDER_CONSTANT))
        pygame.draw.rect(screen.SCREEN,colorObj.color,pygame.Rect(0,0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE))
        pygame.draw.rect(screen.SCREEN,Colors.black,pygame.Rect(0,0,SMALL_BUTTON_SIZE,SMALL_BUTTON_SIZE),SMALL_BUTTON_SIZE // BORDER_CONSTANT)

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                positions.set_new(screen.SCREEN.get_height())
                buttons = color_selection_setup(screen,positions)

            if event.type == pygame.QUIT:
                isRunning = False

        pygame.display.update()


if __name__ == '__main__':
    run()