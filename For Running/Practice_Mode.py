import pygame
import numpy as np
import sys

window_width, window_height = 1000, 650
pygame.init()
display = pygame.display.set_mode((window_width,window_height))
screen = pygame.Surface((window_width,window_height))
icon = a = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Pong Game')

# display = pygame.display.get_surface()


game_font = '8-BIT WONDER.TTF'
WHITE = (255,255,255)
GREY = (100, 100, 100)
GREY2 = (112,128,144)
BLACK = (0, 0, 0)
# pygame.init()

# clock = pygame.time.Clock()


class Background():
    def __init__(self):
        pass
    
    def draw(self):
        pygame.draw.line(pygame.display.get_surface(), Game.FG, (Game.DISPLAY_W//2, 0), (Game.DISPLAY_W//2, Game.DISPLAY_H), 3)
        pygame.draw.circle(display, Game.FG, (Game.DISPLAY_W//2, Game.DISPLAY_H//2), Game.DISPLAY_H//3, width=3)
        pygame.draw.rect(display, Game.FG, (0, 0, Game.DISPLAY_W, Game.BORDER))
        pygame.draw.rect(display, Game.FG, (0, Game.DISPLAY_H-Game.BORDER,
                                                    Game.DISPLAY_W, Game.DISPLAY_H))
        
class Scoreboard():
    def __init__(self, p1_score=0, p2_score=0, font_size=50):
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.font = pygame.font.Font(game_font, font_size)
		
    def display(self, new_p1_score, new_p2_score):
        self.p1_score = new_p1_score
        self.p2_score = new_p2_score
        result_surf = self.font.render('%s      %s' %(self.p1_score, self.p2_score), True, WHITE)
        w, h = result_surf.get_width(), result_surf.get_height()
        x, y = (display.get_width()-w)//2, (display.get_height()-1.5*h)//2
        display.blit(result_surf, (x, y))


class Paddle():
    window_width = display.get_size()
    window_height = display.get_height()
    def __init__(self, x, y, speed=20, width=20, height=150, color=GREY):
        self.DISPLAY = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
    
    def move_up(self):
        if self.y - self.width > 0: self.y -= self.speed
    
    def move_down(self):
        if self.y + self.height + self.width < Paddle.window_height: self.y += self.speed
    
    def move_mouse(self):
        self.y = pygame.mouse.get_pos()[1]
    
    def draw(self):
        pygame.draw.rect(display, self.color,
                         pygame.Rect((self.x, self.y), (self.width, self.height)))
    

class Ball():
    def __init__(self, r, speed, color=WHITE):
        self.x = display.get_width()//2
        self.y = display.get_height()//2
        self.r = r
        self.speed = speed
        self.direction = np.random.uniform(0, 2*np.pi)
        self.vx = self.speed * np.cos(self.direction)
        self.vy = self.speed * np.sin(self.direction)
        # self.vx = 5
        # self.vy = 1
        self.color = WHITE
    
    def move(self):
        pass
    
    def _collision(self, direction=None, crazy=None):
        if self._collision_left() or self._collision_right() or direction:
            self.vx = - self.vx
        if self._collision_up_down():
            self.vy = - self.vy
        if direction and crazy:
            self.vy = direction
        self.x += self.vx
        self.y += self.vy
        
    def _collision_left(self):
        return self.x <= 0
    def _collision_right(self):
        return self.x + self.r >= display.get_width()

    def _collision_up_down(self):
        return self.y - self.r - 20 <= 0 or self.y + self.r >= display.get_height() - 20
    
    def draw(self):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.r)
    
class Game():
    DISPLAY_W = display.get_width()
    DISPLAY_H = display.get_height()
    PADDLE_W = BORDER = 20
    PADDLE_H = 150
    PADDLE_V = 2
    BALL_SIZE = 10
    BALL_V = 1.25
    PHYSX = False
    KEYBOARD = True
    BG = BLACK
    FG = WHITE
    COM = False
    SEC = True
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
        self.move_ball()
        self.draw()
    
    def game_loop(self):
        while self.running: # main game loop
            # clock.tick(100)
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
            
    def apply_settings(self):
        Game.PHYSX = self.settings[0]
        Game.KEYBOARD = self.settings[1]
        Game.COM = self.settings[2]
        Game.SEC = self.settings[3]
        Game.BALL_V = self.settings[4]
                    
    def move_P1(self):
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
        ai = paddle.y + paddle.height//2
        if ai > self.ball.y:
            paddle.move_up()
        if ai < self.ball.y:
            paddle.move_down()
            
    def ball_collision(self):
        if self.ball._collision_left():
            Game.P_S += 1
        if self.ball._collision_right():
            Game.P_F += 1
        if self._paddle_collision(self.P1):
            self.ball._collision(self._speedup(self.P1), Game.PHYSX)

        if self._paddle2_collision(self.P2):
            self.ball._collision(self._speedup(self.P2), Game.PHYSX)
            
    def _paddle_collision(self, paddle):
        collision_x = self.ball.x + self.ball.r >= paddle.x and paddle.x + paddle.width >= self.ball.x
        collision_y = self.ball.y + self.ball.r >= paddle.y and paddle.y + paddle.height >= self.ball.y
        return collision_x and collision_y
    def _paddle2_collision(self, paddle):
        collision_x = self.ball.x >= paddle.x and paddle.x + paddle.width >= self.ball.x - self.ball.r
        collision_y = self.ball.y + self.ball.r >= paddle.y and paddle.y + paddle.height >= self.ball.y
        return collision_x and collision_y
        
    def _speedup(self, paddle):
        ball_pos = self.ball.y + self.ball.r
        paddle_pos = paddle.y + paddle.height//2
        diff = ball_pos - paddle_pos
        return diff / 50       
    
    def move_ball(self):
        self.ball._collision()
        self.ball_collision()
        
    def draw(self):
        self.background.draw()
        self.P1.draw()
        self.P2.draw()
        self.ball.draw()
        self.scoreboard.display(Game.P_F, Game.P_S)        
        
    def pause(self):
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
        
def main():
    game = Game([1, 1, 0, 0, 1.25])
    game.game_loop()

        

main()    
# print(1)