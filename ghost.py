import pygame as pg
import random as r

class Ghost(pg.sprite.Sprite):

    def __init__(self, x, y, floor):
        self.health = 150 * (1 + floor / 10)
        self.x_speed = 0
        self.y_speed = 0
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale_by(pg.image.load("lich.png"), 3)
        self.rect = self.image.get_rect(center = (x, y))
        self.enemy_list = []

    def update(self, player, list, attack):
        if self.rect.x < player.rect.x:
            self.x_speed = 2
        if self.rect.x > player.rect.x:
            self.x_speed = -2
        if self.rect.y < player.rect.y:
            self.y_speed = 2
        if self.rect.y > player.rect.y:
            self.y_speed = -2

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        self.sword_collide(attack, player.damage)

        """if self.health <= 0:
            self.death(list)"""

    def sword_collide(self, attack, damage):
        if attack != None:
            if pg.sprite.collide_rect(self, attack):
                self.health -= damage
                if self.rect.left > attack.rect.left:
                    self.rect.x += 10
                if self.rect.right < attack.rect.right:
                    self.rect.x -= 10


    """def death(self, list):
        list.remove(self)"""

    """def summon(self, floor, rand_min, rand_max):
        for i in range(r.randint(rand_min, rand_max)):
            self.enemy_list.append(self.__init__(r.randint(100, 800), r.randint(100, 800), floor))
        return self.enemy_list"""