import pygame as pg
from settings import *
from random import randint


class Player(pg.sprite.Sprite):
    def __init__(self, game, mapIndex, color):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.mapIndex = mapIndex
        self.image = pg.image.load("images/dwarf.png")
        # self.image.fill(YELLOW)
        # features of the character
        self.health, self.energy, self.hit, self.defense, self.speed = None, None, None, None, None
        self.init_features()
        # positions of the character
        self.rect = self.image.get_rect()
        self.x = randint(2, 10)
        self.y = randint(2, 10)
        self.available_positions = []
        self.pos = self.mapIndex[self.y][self.x][2]
        self.get_available_positions()
        self.pcolor = color

    def init_features(self, health=100, energy=100, hit=5, defense=10, speed=5):
        self.health = health
        self.energy = energy
        self.hit = hit
        self.defense = defense
        self.speed = speed

    def update_features(self, **kwargs):
        for key, value in kwargs.items():
            if key == "health":
                self.health += value
            elif key == "energy":
                self.energy += value
            elif key == "hit":
                self.hit += value
            elif key == "defense":
                self.defense += value
            elif key == "speed":
                self.speed += value

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
        # gets available positions of the player
        self.available_positions = []
        if self.pos == 1:
            for (y_, x_) in (-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1):
                if 0 <= self.y + y_ < len(self.mapIndex) and 0 <= self.x + x_ < len(self.mapIndex[0]):
                    self.available_positions.append((self.y + y_, self.x + x_))
        else:
            for (y_, x_) in (-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, -1):
                if 0 <= self.y + y_ < len(self.mapIndex) and 0 <= self.x + x_ < len(self.mapIndex[0]):
                    self.available_positions.append((self.y + y_, self.x + x_))


class PlayerStatistics(pg.sprite.Sprite):
    def __init__(self, game, x, y, player):
        self.groups = game.all_sprites, game.playerstat_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((370, 20))
        #self.image.fill(LIGHTGREY)
        # self.font = pg.font.SysFont("comicsansmsttf", 15)
        # self.font = pg.font.Font('freesansbold.ttf', 15)
        # self.text = self.font.render(' ', True, RED)
        # self.textRect = self.text.get_rect()
        # self.textRect.center = (x // 2, y // 2)
        # self.image.blit(self.text, self.textRect)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * EDGE
        self.rect.y = y * EDGE
        self.player = player

    def update(self):
        text = "health: " + str(self.player.health) + " " + \
               "energy: " + str(self.player.energy) + " " + \
               "hit: " + str(self.player.hit) + " " + \
               "defense: " + str(self.player.defense) + " " + \
               "speed: " + str(self.player.speed)


        font = pg.font.SysFont("comicsansmsttf", 15)
        text2 = font.render(text, True, self.player.pcolor)
        textRect = text2.get_rect()
        textRect.center = (self.x + text2.get_width() // 2, self.y + text2.get_height() // 2)
        #self.image.subsurface(self.image.get_rect())
        label = font.render(text, 1, self.player.pcolor)
        self.image.fill(LIGHTGREY)
        self.image.blit(label, textRect)
        self.image.blit(text2, textRect)


