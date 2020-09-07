import pygame as pg
from settings import *
from random import randint

class Player(pg.sprite.Sprite):
    def __init__(self, game, mapIndex):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.mapIndex = mapIndex
        self.image = pg.image.load("images/dwarf.png")
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = randint(2, 10)
        self.y = randint(2, 10)
        self.available_positions = []
        self.pos = self.mapIndex[self.y][self.x][2]
        self.get_available_positions()

    def move(self, coord_y, coord_x):
        self.x = coord_x
        self.y = coord_y

    def update(self):
        # updates position of the player on the screen
        if 0 <= self.y < len(self.mapIndex) and 0 <= self.x < len(self.mapIndex[0]):
            self.rect.x = self.mapIndex[self.y][self.x][1] - X_DIST
            self.rect.y = self.mapIndex[self.y][self.x][0] - Y_DIST
            self.pos = self.mapIndex[self.y][self.x][2]

    def get_available_positions(self):
        self.available_positions = []
        if self.pos == 1:
            for (y_, x_) in (-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1):
                if 0 <= self.y + y_ < len(self.mapIndex) and 0 <= self.x + x_ < len(self.mapIndex[0]):
                    self.available_positions.append((self.y + y_, self.x + x_))
        else:
            for (y_, x_) in (-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, -1):
                if 0 <= self.y + y_ < len(self.mapIndex) and 0 <= self.x + x_ < len(self.mapIndex[0]):
                    self.available_positions.append((self.y + y_, self.x + x_))
