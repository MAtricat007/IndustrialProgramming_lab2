import pygame as pg

speed = 5
jump_height = 11
g = 0.25
drop_speed = 15

class Player(pg.sprite.Sprite):

    def __init__ (self, x : int, y : int):
        """
        инициализация персонажа
        """
        self.health = 600
        self.mana = 100
        self.x_speed = 0
        self.y_speed = 0
        self.onGround = False
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale_by(pg.image.load("player_pattern_static_left.png"), 1.5)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, left : bool, right: bool, up : bool, platforms, enemy, floor):
        """
        передвижение персонажа
        """    

        self.damage = 25 * (1 + floor / 15)

        if up:
            if self.onGround:
                self.y_speed = -jump_height
                """self.onGround = False"""

        if not self.onGround:
            self.y_speed += g

        self.onGround = False

        if left:
            self.x_speed = -speed
            self.image = pg.transform.scale_by(pg.image.load("player_pattern_static_left.png"), 1.5)

        if right:
            self.x_speed = speed
            self.image = pg.transform.scale_by(pg.image.load("player_pattern_static_right.png"), 1.5)

        if not left and not right:
            self.x_speed = 0

        self.rect.x += self.x_speed
        self.collide(self.x_speed, 0, platforms)

        self.rect.y += self.y_speed
        self.collide(0, self.y_speed, platforms)

        self.collide_enemy(enemy, floor)

    def collide(self, x_speed, y_speed, platforms):
        for i in platforms:
            if pg.sprite.collide_rect(self, i):

                if x_speed > 0:
                    self.rect.right = i.rect.left

                if x_speed < 0:
                    self.rect.left = i.rect.right

                if y_speed > 0:
                    self.rect.bottom = i.rect.top
                    self.onGround = True
                    self.y_speed = 0
                if y_speed < 0:
                    self.rect.top = i.rect.bottom
                    self.y_speed = 0

    def collide_enemy(self, enemy, floor):
        for i in enemy:
            if pg.sprite.collide_rect(self, i):
                self.health -= 5 * floor * 0.25