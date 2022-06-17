import pygame
import sys
# from abc import ABCMeta, abstractmethod
import abc

window_width, window_height = 1000, 650
pygame.init()
display = pygame.display.set_mode((window_width,window_height))
screen = pygame.Surface((window_width,window_height))
# icon = a = pygame.image.load('ping-pong.png')
# pygame.display.set_icon(icon)
pygame.display.set_caption('Pong Game')

# display = pygame.display.get_surface()


game_font = '8-BIT WONDER.TTF'
font_size = 60
WHITE = (255,255,255)
GREY = (100, 100, 100)
GREY2 = (112,128,144)
BLACK = (0, 0, 0)
# pygame.init()

# clock = pygame.time.Clock()

class Button():
    def __init__(self, text):
        self.text = text
        self.state = False
        
    def draw(self, y, size=font_size):
        myfont = pygame.font.SysFont(game_font, size)
        data = myfont.render(self.text, 1, WHITE)
        w = data.get_width()
        x = (display.get_width() - w)//2
        display.blit(data, (x, y))
        return x
        
    def is_active(self):
        return self.state
    
class Cursor():
    def __init__(self):
        self.marker = "X"
    
    def draw(self, x, y):
        myfont = pygame.font.SysFont('8-BIT WONDER.TTF', font_size)
        data = myfont.render(self.marker, 1, WHITE)
        display.blit(data, (x, y))

class Menu():
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        self.buttons = []
    
    def draw_buttons(self):
        for button in self.buttons:
            pass
    
    @abc.abstractmethod
    def click(self):
        pass
    
    @abc.abstractmethod
    def other(self):
        pass
    
    

class Main(Menu):
    font_height = font_size/1.4
    def __init__(self):
        self.title = 'Python Pong Game'
        self.buttons_text = ['Play Game', 'Settings', ' Credits']
        self.buttons = [Button(i) for i in self.buttons_text]
        self.current_button = 0
        self.cursor = Cursor()
        self.draw()
        
    def draw(self):
        Button(self.title).draw(display.get_height()//7, font_size+20)
        self._draw_buttons()
        
    def _draw_buttons(self):
        number = len(self.buttons)
        y = (display.get_height()-number*Main.font_height)//2
        for button in self.buttons:
            x = button.draw(y)
            if button.is_active():
                self.cursor.draw(x - 50,y)
            y += Main.font_height
    
    def update(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.current_button = (self.current_button+1)//len(self.current_button)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.current_button = (self.current_button-1)
        if pygame.key.get_pressed()[pygame.K_ENTER]:
            self.open()


    
class Play(Menu):
    def __init__(self):
        pass
    
class Settings(Menu):
    def __init__(self):
        pass
    
class Credits(Menu):
    def __init__(self):
        pass
    
    
test = Main()

running = True

while running: # main game loop
    display.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    test.draw()
    pygame.display.flip()
    
    