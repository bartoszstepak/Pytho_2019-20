import pygame


class Player:

    def __init__(self, X, Y, maxX, maxY, speed, lives):
        self.possitionX = X
        self.possitionY = Y
        self.speed = speed
        self.lives = lives
        self.moveRight = 0
        self.moveLeft = 0
        self.moveUp = 0
        self.moveDown = 0
        self.maxX = maxX
        self.maxY = maxY
        self.score = 0;
        self.img = pygame.image.load('musk.png')
        self.canMove = True


    def move_right(self):
        self.moveRight += self.speed

    def move_left(self):
        self.moveLeft -= self.speed

    def move_up(self):
        self.moveUp -= self.speed

    def move_down(self):
        self.moveDown += self.speed

    def stop_moving(self, key):
        if key == pygame.K_RIGHT:
            self.moveRight = 0
        if key == pygame.K_LEFT:
            self.moveLeft = 0
        if key == pygame.K_DOWN:
            self.moveDown = 0
        if key == pygame.K_UP:
            self.moveUp = 0

    def updateMoves(self):
        if self.canMove:
            self.possitionX += self.moveRight
            self.possitionX += self.moveLeft
            self.possitionY += self.moveUp
            self.possitionY += self.moveDown

        self.possitionX = self.update_possition_if_out_of_border(self.possitionX, self.maxX)
        self.possitionY = self.update_possition_if_out_of_border(self.possitionY, self.maxY)

    def stop(self):
        self.canMove = False

    def go(self):
        self.canMove = True

    def update_possition_if_out_of_border(self, possition, max):
        if possition < 0:
            return 0
        elif possition >= max:
            return max
        else:
            return possition

    def kill(self):
        self.possitionX = 350
        self.possitionY = 500
        self.lives -= 1
