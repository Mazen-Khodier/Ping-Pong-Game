# Importing Libraries
import pygame
import numpy as np
import sys

# This line is supposed to be run when the file is called from the "Menus.py"
# To be implemented in the future instead of instantiating the screen here
# display = pygame.display.get_surface()

# Lines that should be in the file "Menus.py":
pygame.init()
window_width, window_height = 1000, 650
display = pygame.display.set_mode((window_width,window_height))
screen = pygame.Surface((window_width,window_height))
icon = a = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Pong Game')
game_font = '8-BIT WONDER.TTF'
WHITE = (255,255,255)
GREY = (100, 100, 100)
GREY2 = (112,128,144)
BLACK = (0, 0, 0)

# This line is used for controlling the speed of the game
# May be added as a customizable setting in the future
# clock = pygame.time.Clock()

class Background():
    """
    DESCRIPTION:
    A class for bakcground objects
    currently it is only used for drawing the field borders and centerfield
    but is left for possible additions in the future like images and other customizable settings
    """
    def __init__(self):
        pass
    
    def draw(self, color, thickness):
        display = pygame.display.get_surface()
        w, h = display.get_width(), display.get_height()
        pygame.draw.line(display, color, (w//2, 0), (w//2, h), 3)
        pygame.draw.circle(display, color, (w//2, h//2), h//3, width=3)
        pygame.draw.rect(display, color, (0, 0, w, thickness))
        pygame.draw.rect(display, color, (0, h-thickness, w, h))
        
        
class Scoreboard():
    """
    DESCRIPTION:
    Keeps track of scores during games
    
    ATTRIBUTES:
    p1_score: Player 1 current score
    p2_score: Player 2 current score
    font: used font for writing scores
    """
    def __init__(self, p1_score=0, p2_score=0, font_size=50):
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.font = pygame.font.Font(game_font, font_size)
		
    def display(self, new_p1_score, new_p2_score):
        """
        Main Scoreboard method for diplaying the scores of both players on the screen
        """
        self.p1_score = new_p1_score
        self.p2_score = new_p2_score
        result_surf = self.font.render('%s      %s' %(self.p1_score, self.p2_score), True, WHITE)
        w, h = result_surf.get_width(), result_surf.get_height()
        x, y = (display.get_width()-w)//2, (display.get_height()-1.5*h)//2
        display.blit(result_surf, (x, y))


class Paddle():
    """
    DESCRIPTION:
    The objects which players use to play
    
    ATTRIBUTES:
    x: the x co-ordinate of the top left side of the paddle
    y: the x co-ordinate of the top left side of the paddle
    width: the width of the paddle
    height: the height of the paddle
    speed: the speed of the paddle when using the keyboaed for moving
    color: The color used for drawing the paddle (default is grey)
    """
    window_width = display.get_size()
    window_height = display.get_height()
    def __init__(self, x, y, speed=20, width=20, height=150, color=GREY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
    
    def move_up(self):
        """
        For playing using a keyboard
        Moves the paddle up while ensuring it does NOT go out of bounds
        """
        if self.y - self.width > 0: self.y -= self.speed
    
    def move_down(self): # Similar to move_up method
        if self.y + self.height + self.width < Paddle.window_height: self.y += self.speed
    
    def move_mouse(self):
        """
        For playing using the mouse
        """
        self.y = pygame.mouse.get_pos()[1]
    
    def draw(self): # draws the paddles
        pygame.draw.rect(display, self.color,
                         pygame.Rect((self.x, self.y), (self.width, self.height)))
    

class Ball():
    """
    DESCRIPTION:
    The objects which players use to play
    
    ATTRIBUTES:
    x: the x co-ordinate of the center of the ball
    y: the y co-ordinate of the center of the ball
    r: the radius of the ball
    speed: the total speed of the ball
    vx: the x component of the ball speed
    vy: the y component of the ball sped
    color: the color used for drawing the ball (default is white)
    """
    def __init__(self, r, speed, color=WHITE):
        self.x = display.get_width()//2
        self.y = display.get_height()//2
        self.r = r
        self.speed = speed
        direction = np.random.uniform(0, 2*np.pi) # for starting the ball in a random direction
        self.vx = self.speed * np.cos(direction)
        self.vy = self.speed * np.sin(direction)
        self.color = WHITE
    
    def collision(self, direction=None, crazy=None):
        """
        Private method for checking collisions of the ball with other objects
        like paddles and background borders
        """
        if self.collision_left() or self.collision_right() or direction:
            self.vx = - self.vx # invert the ball direction in the x-axis
        if self._collision_up_down():
            self.vy = - self.vy # invert the ball direction in the y-axis
        if direction and crazy: # check for PHYSX settings
            self.vy = direction
        # update the ball posistion every frame
        self.x += self.vx
        self.y += self.vy
        
    def collision_left(self): # checks for collision with left side
        return self.x <= 0
    def collision_right(self): # checks for collision with right side
        return self.x + self.r >= display.get_width()

    def _collision_up_down(self): # private method for checking up and down collisions
        return self.y - self.r - 20 <= 0 or self.y + self.r >= display.get_height() - 20
    
    def draw(self): # method for drawing the ball on the screen
        pygame.draw.circle(display, self.color, (self.x, self.y), self.r)
    
class Game():
    """
    DESCRIPTION:
    The main class of the program. Used for interactions between all the previous
    objects and contains the game logic
    
    ATTRIBUTES:
    running: Attribute for knowing the current state of the program
            Should be used when interacting with main menu file
    
    settings: A list of Zeros and Ones which stands for various customizable settings
                of different game modes. A 1 means the setting is enabled and vice versa

    P1: Player 1, an instance of the Paddle class
    P2: Player 2, an instance of the Paddle class
    ball: An instance of the Ball class for playing
    scoreboard: An instance of the Scoreboard class for tracking players scores
    background: An instance of the Background class with specific customizable settings
    
    
    CLASS VARIABLES:
    """
    DISPLAY_W = display.get_width()
    DISPLAY_H = display.get_height()
    BORDER = 20 # Background Borders Width 
    PADDLE_W = 20 # Width of the paddles to be used
    PADDLE_H = 150 # Height of the paddles to be used
    PADDLE_V = 2 # Speed of the paddles to be used
    BALL_SIZE = 10 # Size pf the ball to be used
    BALL_V = 1.25 # Speed of the ball to be used
    PHYSX = True # Simple/Advanced Physics Setting
    KEYBOARD = True # Keyboard/Mouse Setting
    BG = BLACK # Background Color
    FG = WHITE # Foreground Color
    COM = False # AI Setting
    SEC = True # Singleplayer/Multiplayer Setting
    P_S = P_F = 0
    
    def __init__(self, settings = [1, 1, 0, 1, 1.25]):
        self.running = True
        self.settings = settings
        self.apply_settings()
        self.P1 = Paddle(Game.DISPLAY_W - Game.PADDLE_W, Game.DISPLAY_H//2-Game.PADDLE_H//2, Game.PADDLE_V)
        self.P2 = Paddle(0, Game.DISPLAY_H//2-Game.PADDLE_H//2, Game.PADDLE_V)
        self.ball = Ball(Game.BALL_SIZE, Game.BALL_V)
        self.scoreboard = Scoreboard(0)
        self.background = Background()
    
    def apply_settings(self):
        """
        Method for modifying the class variables which stand for settings
        (This method is yet to be used effectively until fixing files interactions)
        All Game Class Variables may be added here but for now,
        only the most important ones are currently added
        """
        Game.PHYSX = self.settings[0]
        Game.KEYBOARD = self.settings[1]
        Game.COM = self.settings[2]
        Game.SEC = self.settings[3]
        Game.BALL_V = self.settings[4]
    
    def game_loop(self):
        """
        Main method of the Game class
        An infinite loop for constantly checking for user input and updating
        the display appropriately
        """
        while self.running:
            # clock.tick(100) ## for controlling game speed (testing/future settings)
            display.fill(self.BG)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()
            self.move_P1()
            self.move_P2()
            self.move_ball()
            self.draw()
            pygame.display.flip()     
            
    def pause(self):
        """
        Method for pausing the main game loop by entering another loop until
        the user decides to continue (or exit) the game
        """
        pause_screen = True
        while pause_screen:
            self.draw()
            self._pause_msg()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pause_screen = False
                    else:
                        pause_screen = False
            
    def _pause_msg(self):
        """
        Private method for handling printing the pause message details without
        unnecessarily complicating the pause method
        """
        myfont1 = pygame.font.SysFont(game_font, 100)
        myfont2 = pygame.font.SysFont(game_font, 45)
        msg1 = myfont1.render("Game Paused", 1, GREY2)
        msg2 = myfont2.render("Press Esc to exit", 1, GREY2)
        msg3 = myfont2.render("Press any other key to continue", 1, GREY2)
        w1, h1 = msg1.get_width(), msg1.get_height()
        w2, h2 = msg2.get_width(), msg2.get_height()
        w3, h3 = msg3.get_width(), msg3.get_height()
        x1, y1 = (display.get_width() - w1+5)//2, (display.get_height())//10
        display.blit(msg1, (x1, y1))
        display.blit(msg2, (x1+w1//2-w2//2, y1+(h1+h2)))
        display.blit(msg3, (x1+w1//2-w3//2, y1+(h1+h2+h3)))
                    
    def move_P1(self):
        """
        Check for current settings and moves player 1 accordingly (keyboard or mouse)
        Also checks whether the player 1 is set to be the AI instead
        """
        if Game.COM and not Game.SEC:
            self.move_ai(self.P1)
        else:
            if Game.KEYBOARD:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.P1.move_up()
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.P1.move_down()
            else:
                self.P1.move_mouse()
            
    def move_P2(self):
        """
        Check for current settings and modifies player 2 accordingly (single or multiplayer)
        Also checks whether the player 2 is set to be the AI instead
        """
        if not Game.COM and Game.SEC:
            if pygame.key.get_pressed()[pygame.K_w]:
                self.P2.move_up()
            if pygame.key.get_pressed()[pygame.K_s]:
                self.P2.move_down()
        elif not Game.SEC:
            self.P2.height = display.get_height()
            self.P2.y = 0
            self.P2.color = Game.FG
        else:
            self.move_ai(self.P2)
                
    def move_ai(self, paddle):
        """
        Method for AI playing logic
        (Simple algorithm for following the ball instead of the nearest Kneighbours approach)
        """
        ai = paddle.y + paddle.height//2
        if ai > self.ball.y:
            paddle.move_up()
        if ai < self.ball.y:
            paddle.move_down()
    
    def move_ball(self):
        """
        Method for calling necessary methods for handling ball movement
        """
        self.ball.collision()
        self.ball_collision()
    
    def ball_collision(self):
        """
        handles ball-paddles collisions appropriately using ptivate methods
        """
        if self.ball.collision_left():
            Game.P_S += 1
        if self.ball.collision_right():
            Game.P_F += 1
        if self._paddle_collision(self.P1):
            self.ball.collision(self._speedup(self.P1), Game.PHYSX)

        if self._paddle2_collision(self.P2):
            self.ball.collision(self._speedup(self.P2), Game.PHYSX)
            
    def _paddle_collision(self, paddle): # Collision with player 1
        collision_x = self.ball.x + self.ball.r >= paddle.x and paddle.x + paddle.width >= self.ball.x
        collision_y = self.ball.y + self.ball.r >= paddle.y and paddle.y + paddle.height >= self.ball.y
        return collision_x and collision_y
    def _paddle2_collision(self, paddle): # Collision with player 2
        collision_x = self.ball.x >= paddle.x and paddle.x + paddle.width >= self.ball.x - self.ball.r
        collision_y = self.ball.y + self.ball.r >= paddle.y and paddle.y + paddle.height >= self.ball.y
        return collision_x and collision_y
        
    def _speedup(self, paddle):
        """
        Private method for calculating distance from paddle center upon collision
        used for advanced physics settings
        """
        ball_pos = self.ball.y + self.ball.r
        paddle_pos = paddle.y + paddle.height//2
        diff = ball_pos - paddle_pos
        return diff / 50       
    
    def draw(self):
        """
        method for drawing all objects on the screen
        """
        self.background.draw(Game.FG, Game.BORDER)
        self.P1.draw()
        self.P2.draw()
        self.ball.draw()
        self.scoreboard.display(Game.P_F, Game.P_S)      

       
def run_main():
    game = Game()
    game.game_loop()
    
run_main()