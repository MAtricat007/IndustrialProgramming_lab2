import pygame as pg
        
  
class Healthbar_red(pg.sprite.Sprite):

    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 10))
        self.image.fill((255, 0, 0))
        self.rect = pg.Rect(player.rect.x, player.rect.y - 12, 40, 10)
        
        
class Healthbar_green(pg.sprite.Sprite):

    def __init__(self, player):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((player.health // 15, 10))
        self.image.fill((0, 255, 0))
        self.rect = pg.Rect(player.rect.x, player.rect.y - 12, player.health // 15, 10)

