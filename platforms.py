import pygame as pg

class Platform(pg.sprite.Sprite):
    """
    Чтобы создать платформу, нужно создать объект Platform(<Координата Х>, <Координата У>, <Файл с текстурой>)
    Координаты указываются для левого верхнего угла платформы
    
    Чтобы платформа появилась на экране, нужно применить к объекту метод draw(<Действующий экран>)
    """

    def __init__(self, x : int, y : int, filename : str):
        """
        инициализация палтформы
        """
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename)
        self.rect = self.image.get_rect(center = (x, y))

    def draw(self, screen):
        """
        отрисовка платформы на экране
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))