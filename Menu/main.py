from game import Game

g = Game()

while g.RUNNING:
    g.curr_menu.display_menu()
    g.game_loop()
