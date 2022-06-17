from menu import *


class Game:
    def __init__(self):
        pygame.init()
        self.RUNNING, self.PLAYING = (True, False)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.W_KEY, self.S_KEY = False, False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H, self.BORDER = 1200, 600, 20
        self.DISPLAY = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.WINDOW = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.FONT_NAME = "8-BIT WONDER.TTF"
        # self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE, self.RED, self.GREEN, self.BLUE = (
            (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255))
        self.BACKGROUND_COLOR = self.BLACK
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.game_menu = GameMenu(self)
        self.curr_menu = self.main_menu
        self.TYPE = 0
        self.RECT_1 = pygame.draw.rect(self.WINDOW, self.WHITE, pygame.Rect((0, 0), (self.DISPLAY_W, self.BORDER)))
        self.RECT_2 = pygame.draw.rect(self.WINDOW, self.WHITE, pygame.Rect((0, 0), (self.BORDER, self.DISPLAY_H)))
        self.RECT_3 = pygame.draw.rect(self.WINDOW, self.WHITE,
                                       pygame.Rect((0, self.DISPLAY_H), (self.DISPLAY_W, self.BORDER)))
        # ball
        self.RADIUS = 20
        self.BALL_X, self.BALL_Y, self.BALL_X_SPEED, self.BALL_Y_SPEED = self.DISPLAY_W - self.RADIUS - 20, self.DISPLAY_H // 2, -.3, .3
        self.A = .05

        self.BALL = pygame.draw.circle(self.WINDOW, self.WHITE, (self.BALL_X, self.BALL_Y), self.RADIUS)
        self.PADDLE_X, self.PADDLE_Y = self.DISPLAY_W - 10, self.DISPLAY_H // 2
        self.PADDLE = pygame.draw.rect(self.WINDOW, self.WHITE, pygame.Rect((self.DISPLAY_W - 20, self.DISPLAY_H - 100),
                                                                            (self.BORDER, self.DISPLAY_H)))

    def game_loop(self):
        while self.PLAYING:
            self.check_events()
            if self.BACK_KEY:
                self.PLAYING = False
            self.DISPLAY.fill(self.BACKGROUND_COLOR)
            if self.TYPE == 1:

                self.solo()



            elif self.TYPE == 2:
                self.vs_com()


            elif self.TYPE == 3:
                self.duo()

    # self.draw_text('you lost Thanks for Playing', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
    # self.WINDOW.blit(self.DISPLAY, (0, 0))
    # pygame.display.update()
    # self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING, self.PLAYING = (False, False)
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_w:
                    self.W_KEY = True
                if event.key == pygame.K_s:
                    self.S_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.RIGHT_KEY, self.LEFT_KEY, self.START_KEY, self.BACK_KEY = (
            False, False, False, False, False, False)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.FONT_NAME, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.DISPLAY.blit(text_surface, text_rect)

    def vs_com(self):
        pass

    def duo(self):
        pass

    def make_ball_at_start(self):

        self.Paddle()
        self.BALL_X = self.BALL_X + self.BALL_X_SPEED
        self.BALL_Y = self.BALL_Y + self.BALL_Y_SPEED
        self.BALL = pygame.draw.circle(self.WINDOW, self.WHITE, (self.BALL_X, self.BALL_Y), self.RADIUS)
        pygame.draw.rect(self.WINDOW, self.WHITE, pygame.Rect((0, 0), (self.DISPLAY_W, self.BORDER)))
        pygame.draw.rect(self.WINDOW, self.WHITE, pygame.Rect((0, 0), (self.BORDER, self.DISPLAY_H)))
        pygame.draw.rect(self.WINDOW, self.WHITE,
                         pygame.Rect((0, self.DISPLAY_H - self.BORDER), (self.DISPLAY_W, self.BORDER)))
        pygame.display.flip()
        self.BALL = pygame.draw.circle(self.WINDOW, self.BACKGROUND_COLOR, (self.BALL_X, self.BALL_Y), self.RADIUS)
        self.BALL_X = self.BALL_X + self.BALL_X_SPEED
        self.BALL_Y = self.BALL_Y + self.BALL_Y_SPEED
        newx = self.BALL_X
        newy = self.BALL_Y
        if newx <= self.BORDER + self.RADIUS:
            self.BALL_X_SPEED = -self.BALL_X_SPEED
        elif newy <= self.BORDER + self.RADIUS or newy >= self.DISPLAY_H - self.BORDER - self.RADIUS:
            self.BALL_Y_SPEED = -self.BALL_Y_SPEED
        elif newx > self.DISPLAY_W - self.BORDER - self.RADIUS and abs((newy-50)-self.PADDLE_Y) <120//2:
            if self.BALL_X_SPEED > 0 and self.BALL_Y_SPEED > 0:
                self.BALL_Y_SPEED += self.A
                self.BALL_X_SPEED += self.A
            self.BALL_X_SPEED = -self.BALL_X_SPEED


        elif newx > self.DISPLAY_W:
            self.PLAYING = False


        print(newx, newy)
    def move_ball(self):
        while self.PLAYING:
            self.BALL_MOVE_X = self.BALL_X + self.BALL_X_SPEED
            self.BALL_MOVE_Y = self.BALL_Y + self.BALL_Y_SPEED

    def Paddle(self):
        pygame.draw.rect(self.WINDOW, self.BACKGROUND_COLOR,
                         pygame.Rect((self.DISPLAY_W - 20, self.PADDLE_Y), (self.BORDER, 100)))
        self.PADDLE_Y = pygame.mouse.get_pos()[1]
        pygame.draw.rect(self.WINDOW, self.WHITE,
                         pygame.Rect((self.DISPLAY_W - 20, self.PADDLE_Y), (self.BORDER, 100)))

    def solo(self):

        self.WINDOW.blit(self.DISPLAY, (0, 0))
        pygame.display.update()
        while self.PLAYING:
            pygame.event.get()
            self.make_ball_at_start()
        self.game_over()
        self.BALL_X, self.BALL_Y, self.BALL_X_SPEED, self.BALL_Y_SPEED = self.DISPLAY_W - self.RADIUS - 20, self.DISPLAY_H // 2, -.3, .3
        self.curr_menu.display_menu()

    def game_over(self):
        while self.RUNNING:
            self.check_events()
            self.draw_text('you lost Thanks for Playing', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
            self.WINDOW.blit(self.DISPLAY, (0, 0))
            pygame.display.update()
            self.reset_keys()
            if self.BACK_KEY:
                return pygame.quit()
            elif self.START_KEY:
                self.game_loop()

