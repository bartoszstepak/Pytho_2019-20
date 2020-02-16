import pygame


class Bullet:

    def __init__(self, X, Y, speed):
        self.possitionX = X
        self.possitionY = Y
        self.speed = speed
        self.move_in_X = speed
        self.move_in_Y = 0
        self.fired = False
        self.img = pygame.image.load('bullet.png')

    def fire(self, X, Y):
        if self.fired is False:
            self.possitionX = X + 40
            self.possitionY = Y + 15
            self.fired = True
        elif self.possitionY < 0:
            self.fired = False
            self.possitionY -= self.speed

    def restrt_possition(self, X, Y):
        self.possitionX = X + 40
        self.possitionY = Y + 15
        self.fired = False
