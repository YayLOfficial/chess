import pygame

from pieces.pieces import Pieces


class Queen(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color

    def isLegalMove(self, y, x, isMovingPiece=False):
        if self.isBetween(y, x, self): return False
        if self.row == y or self.col == x: return True
        if y - self.row == x - self.col or y - self.row == -1 * (x - self.col): return True
        return False

    def render(self, x, y):
        x, y = self.tiles.getCoords(x, y)

        rotImg = pygame.transform.rotate(self.queen[self.color], 0)
        img = self.queen[self.color].get_rect(center=self.queen[self.color].get_rect(topleft=(x+3, y)).center)
        self.win.blit(rotImg, img.topleft)
