import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.MID_W, self.MID_H = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.RUN_DISPLAY = True
        self.CURSOR_RECT = pygame.Rect(0, 0, 20, 20)
        self.OFFSET = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.CURSOR_RECT.x, self.CURSOR_RECT.y)

    def blit_screen(self):
        self.game.WINDOW.blit(self.game.DISPLAY, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = "Start"
        self.START_X, self.START_Y = self.MID_W, self.MID_H + 30
        self.OPTIONS_X, self.OPTIONS_Y = self.MID_W, self.MID_H + 50
        self.credits_X, self.credits_y = self.MID_W, self.MID_H + 70
        self.Quit_X,self.Quit_Y = self.MID_W,self.MID_H+200
        self.CURSOR_RECT.midtop = (self.START_X + self.OFFSET, self.START_Y)

    def display_menu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.check_events()
            self.check_input()
            self.game.DISPLAY.fill(self.game.BACKGROUND_COLOR)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text("Start Game", 20, self.START_X, self.START_Y)
            self.game.draw_text("Options", 20, self.OPTIONS_X, self.OPTIONS_Y)
            self.game.draw_text("Credits", 20, self.credits_X, self.credits_y)
            self.game.draw_text("Quit", 20, self.Quit_X, self.Quit_Y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.STATE == 'Start':
                self.CURSOR_RECT.midtop = (self.OPTIONS_X + self.OFFSET, self.OPTIONS_Y)
                self.STATE = 'Options'
            elif self.STATE == 'Options':
                self.CURSOR_RECT.midtop = (self.credits_X + self.OFFSET, self.credits_y)
                self.STATE = 'Credits'
            elif self.STATE == 'Credits':
                self.CURSOR_RECT.midtop = (self.Quit_X + self.OFFSET, self.Quit_Y)
                self.STATE = 'Quit'
            elif self.STATE == 'Quit':
                self.CURSOR_RECT.midtop = (self.START_X + self.OFFSET, self.START_Y)
                self.STATE = 'Start'
        elif self.game.UP_KEY:
            if self.STATE == 'Quit':
                self.CURSOR_RECT.midtop = (self.credits_X + self.OFFSET, self.credits_y)
                self.STATE = 'Credits'
            elif self.STATE == 'Start':
                self.CURSOR_RECT.midtop = (self.Quit_X + self.OFFSET, self.Quit_Y)
                self.STATE = 'Quit'
            elif self.STATE == 'Options':
                self.CURSOR_RECT.midtop = (self.START_X + self.OFFSET, self.START_Y)
                self.STATE = 'Start'
            elif self.STATE == 'Credits':
                self.CURSOR_RECT.midtop = (self.OPTIONS_X + self.OFFSET, self.OPTIONS_Y)
                self.STATE = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.STATE == 'Start':
                self.game.curr_menu = self.game.game_menu
            elif self.STATE == 'Options':
                self.game.curr_menu = self.game.options
            elif self.STATE == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.STATE == "Quit":
                return pygame.quit()
            self.RUN_DISPLAY = False




class GameMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'Solo'
        self.SOLO_X, self.SOLO_Y = self.MID_W, self.MID_H + 30
        self.VS_COM_X, self.VS_COM_Y = self.MID_W, self.MID_H + 50
        self.duo_X, self.duo_Y = self.MID_W, self.MID_H + 70
        self.CURSOR_RECT.midtop = (self.SOLO_X + self.OFFSET, self.SOLO_Y)

    def display_menu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.check_events()
            self.check_input()
            self.game.DISPLAY.fill(self.game.BACKGROUND_COLOR)
            self.game.draw_text('Game Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Solo", 15, self.SOLO_X, self.SOLO_Y)
            self.game.draw_text("P1 VS COM", 15, self.VS_COM_X, self.VS_COM_Y)
            self.game.draw_text("P1 VS P2", 15, self.duo_X, self.duo_Y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.RUN_DISPLAY = False
        elif self.game.UP_KEY:
            if self.STATE == 'Solo':
                self.STATE = 'duo'
                self.CURSOR_RECT.midtop = (self.duo_X + self.OFFSET, self.duo_Y)
            elif self.STATE == 'Com':
                self.STATE = 'Solo'
                self.CURSOR_RECT.midtop = (self.SOLO_X + self.OFFSET, self.SOLO_Y)
            elif self.STATE == 'duo':
                self.STATE = 'Com'
                self.CURSOR_RECT.midtop = (self.VS_COM_X + self.OFFSET, self.VS_COM_Y)
        elif self.game.DOWN_KEY:
            if self.STATE == 'Solo':
                self.STATE = 'Com'
                self.CURSOR_RECT.midtop = (self.VS_COM_X + self.OFFSET, self.VS_COM_Y)
            elif self.STATE == 'Com':
                self.STATE = 'duo'
                self.CURSOR_RECT.midtop = (self.duo_X + self.OFFSET, self.duo_Y)
            elif self.STATE == 'duo':
                self.STATE = 'Solo'
                self.CURSOR_RECT.midtop = (self.SOLO_X + self.OFFSET, self.SOLO_Y)
        elif self.game.START_KEY:
            if self.STATE == "Solo":
                self.game.TYPE = 1
                self.game.PLAYING = True
                self.RUN_DISPLAY = False


            elif self.STATE == "Com":
                self.game.TYPE = 2
                self.game.PLAYING = True
                self.RUN_DISPLAY = False

            elif self.STATE == "duo":
                self.game.TYPE = 3
                self.game.PLAYING = True
                self.RUN_DISPLAY = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.STATE = 'Background'
        self.BACKGROUND_X, self.BACKGROUND_Y = self.MID_W, self.MID_H + 60
        self.PADDLE_X, self.PADDLE_Y = self.MID_W, self.MID_H + 100
        self.CURSOR_RECT.midtop = (self.BACKGROUND_X + self.OFFSET, self.BACKGROUND_Y)
        self.num = -1

    def display_menu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.check_events()
            self.check_input()
            self.game.DISPLAY.fill(self.game.BACKGROUND_COLOR)
            self.game.draw_text('Options', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text("Color", 30, self.BACKGROUND_X, self.BACKGROUND_Y)
            self.game.draw_text("Paddle", 30, self.PADDLE_X, self.PADDLE_Y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.RUN_DISPLAY = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.STATE == 'Background':
                self.STATE = 'Paddle'
                self.CURSOR_RECT.midtop = (self.PADDLE_X + self.OFFSET, self.PADDLE_Y)
            elif self.STATE == 'Paddle':
                self.STATE = 'Background'
                self.CURSOR_RECT.midtop = (self.BACKGROUND_X + self.OFFSET, self.BACKGROUND_Y)
        elif self.game.START_KEY:
            if self.STATE == "Background":
                if self.num == 3:
                    self.num = -1
                self.num += 1
                x = [self.game.RED, self.game.BLUE, self.game.GREEN, self.game.BLACK]
                self.game.BACKGROUND_COLOR = x[self.num]
                pygame.display.update()


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.RUN_DISPLAY = True
        while self.RUN_DISPLAY:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.RUN_DISPLAY = False
            self.game.DISPLAY.fill(self.game.BACKGROUND_COLOR)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text('Made by THE 3 Ma', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
