import pygame as pg
import sys
from settings import *
from sprites import *
from tilemap import *
from player import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.turn = 1

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.map = TileMap(self.screen)
        self.player1 = Player(self, self.map.mapIndex)
        self.player2 = Player(self, self.map.mapIndex)
        #for x in range(10, 20):
        #    Wall(self, x, 5)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        #self.draw_grid()
        self.map.draw_hexagons() # draws map

        self.player1.get_available_positions()
        self.map.draw_available_positions(self.player1.available_positions)

        self.player2.get_available_positions()
        self.map.draw_available_positions(self.player2.available_positions)

        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONUP:
                (x, y) = pg.mouse.get_pos()
                if self.turn == 1:
                    for (neig_y, neig_x) in self.player1.available_positions:
                        map_y = self.map.mapIndex[neig_y][neig_x][0]
                        map_x = self.map.mapIndex[neig_y][neig_x][1]
                        if abs(y - map_y) < Y_DIST and abs(x - map_x) < X_DIST:
                            self.player1.move(neig_y, neig_x)
                            self.turn = 2
                            break
                elif self.turn == 2:
                    for (neig_y, neig_x) in self.player2.available_positions:
                        map_y = self.map.mapIndex[neig_y][neig_x][0]
                        map_x = self.map.mapIndex[neig_y][neig_x][1]
                        if abs(y - map_y) < Y_DIST and abs(x - map_x) < X_DIST:
                            self.player2.move(neig_y, neig_x)
                            self.turn = 1
                            break

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()