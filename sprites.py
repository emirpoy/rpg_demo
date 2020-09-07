import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = pg.image.load("images/dwarf.png")
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        print("x dist: " , self.x * (X_DIST + X_DIST / 2))
        print("y dist: ", self.y * (Y_DIST * 2))
        self.rect.x = self.x * X_DIST  #* (Y_DIST * 2)
        self.rect.y = self.y * Y_DIST #* (X_DIST + X_DIST / 2)