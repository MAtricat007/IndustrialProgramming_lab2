import pygame as pg

class Mele_attack(pg.sprite.Sprite):

    def __init__(self, player, direction):
        self.direction = direction
        pg.sprite.Sprite.__init__(self)
        if direction == "left" or direction == "":
            self.image = pg.transform.scale_by(pg.image.load("sword_swing_left_final.png"), 2.5)
            '''self.image = pg.transform.scale(pg.transform.rotate(pg.image.load("sword_swing_left.png"), 30), (60, 55))'''
            self.rect = self.image.get_rect(topright=(player.rect.x + 10, player.rect.y - 5))
        if direction == "right":
            self.image = pg.transform.flip(pg.transform.scale_by(pg.image.load("sword_swing_left_final.png"), 2.5), True, False)
            self.rect = self.image.get_rect(topleft=(player.rect.topright[0] - 10, player.rect.topright[1] - 5))

    def update(self, player):
        if self.direction == "left":
            """self.image = pg.transform.rotate(self.image, 10)"""
            self.rect.topright = (player.rect.x, player.rect.y)

        elif self.direction == "right":
            self.rect.x = player.rect.topright[0]
            self.rect.y = player.rect.topright[1]
            """self.image = pg.transform.rotate(self.image, -10)"""