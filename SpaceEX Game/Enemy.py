import pygame
import Helper


class Enemy:

    def __init__(self, X, Y, maxX, maxY, speed):
        self.possitionX = X
        self.possitionY = Y
        self.speed = speed
        self.move_in_X = speed
        self.move_in_Y = 0
        self.maxX = maxX
        self.maxY = maxY
        self.img = pygame.image.load('sat.png')
        self.size = 64

    def move(self):
        self.possitionX += self.move_in_X

        if self.possitionX < 0:
            self.move_in_X = self.speed
            self.possitionY += 20
        if self.possitionX > self.maxX:
            self.move_in_X = -self.speed
            self.possitionY += 20
