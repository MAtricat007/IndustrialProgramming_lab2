import pygame as pg

class Healthbar_red(pg.sprite.Sprite):

    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 10))
        self.image.fill((255, 0, 0))
        self.rect = pg.Rect(player.rect.x, player.rect.y - 12, 40, 10)