import pygame as pg
import sys
from settings import *
from sprites import *

class TileMap:
    def __init__(self, screen):
        self.mapIndex = []
        self.screen = screen
        self.draw_hexagons()

    def draw_hexagons(self):
        self.mapIndex = []
        for y in range(Y_DIST, HEIGHT - Y_DIST, Y_DIST * 2):
            pos = 0
            row = []
            for x in range(X_DIST, WIDTH - X_DIST, X_DIST + X_DIST // 2):
                if pos == 0:
                    self.draw_hex_tile(y, x)
                    row.append((y,x, 0))
                    pos = 1
                else:
                    self.draw_hex_tile(y + Y_DIST, x)
                    row.append((y + Y_DIST, x, 1))
                    pos = 0
            self.mapIndex.append(row)

    def draw_hex_tile(self, y, x, color=LIGHTGREY):
        # draws an hexagonal based on the given x,y coordinates
        # - \ / - \ /
        pg.draw.line(self.screen, color, (x - X_DIST / 2, y + Y_DIST), (x + X_DIST / 2, y + Y_DIST))
        pg.draw.line(self.screen, color, (x + X_DIST / 2, y + Y_DIST), (x + X_DIST, y))
        pg.draw.line(self.screen, color, (x + X_DIST, y), (x + X_DIST / 2, y - Y_DIST))
        pg.draw.line(self.screen, color, (x + X_DIST / 2, y - Y_DIST), (x - X_DIST / 2, y - Y_DIST))
        pg.draw.line(self.screen, color, (x - X_DIST / 2, y - Y_DIST), (x - X_DIST, y))
        pg.draw.line(self.screen, color, (x - X_DIST, y), (x - X_DIST / 2, y + Y_DIST))

    def draw_available_positions(self, avail_pos, color):
        # draws different color for the available spots
        # avail_pos: List[List[int]]
        for (y, x) in avail_pos:
            self.draw_hex_tile(self.mapIndex[y][x][0], self.mapIndex[y][x][1], color)

    def draw_mountains(self):
        pass

    def draw_rivers(self):
        pass