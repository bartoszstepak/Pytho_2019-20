import pygame
import random
import Helper

from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from pygame import mixer


pygame.init()

runningGameLoop = True
game_over = False

screenWidth = 800
screenHeigth = 600
num_of_enemies = 5


screen = pygame.display.set_mode((screenWidth, screenHeigth))

pygame.display.set_caption('SpaceEX')
name_game_logo = pygame.image.load('name-game-logo.png')
pygame.display.set_icon(name_game_logo)
background = pygame.image.load('space.png')

bigFont = pygame.font.SysFont("Times", 60, "bold")
smallFont = pygame.font.SysFont("Times", 30)

player = None
enemies = []
bullet = None


def init_player():
    return Player(350, 500, screenWidth - 85, screenHeigth - 85, 6, 1)


def init_enemies(x):
    enemies = []
    for i in range(num_of_enemies):
        enemy = Enemy(random.randint(0, screenWidth-2), random.randint(50, 150), screenWidth - 64, screenHeigth - 64,
                      random.randint(1, 3))
        enemies.append(enemy)

    return enemies


def init_game():
    global player, enemies, bullet
    player = init_player()
    enemies = init_enemies(num_of_enemies)
    bullet = Bullet(0, 0, 15)


def draw_object(img, x, y):
    screen.blit(img, (x, y))


def move_enemies():
    for enemy in enemies:
        enemy.move()
        isShotted = Helper.isCollision(enemy.possitionX, enemy.possitionY, bullet.possitionX, bullet.possitionY,
                                       30)
        draw_object(enemy.img, enemy.possitionX, enemy.possitionY)

        if isShotted:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            index = enemies.index(enemy)
            enemies.pop(index)
            player.score += 1
            bullet.restrt_possition(player.possitionX, player.possitionY)

        isKilledByEnemy = Helper.isCollision(enemy.possitionX, enemy.possitionY, player.possitionX,
                                             player.possitionY,
                                             60)
        if isKilledByEnemy:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            player.kill()

        if enemy.possitionY > 550:
            print(enemy.possitionY)
            index = enemies.index(enemy)
            enemies.pop(index)
            player.score -= 1


def fire_bullet():
    if bullet.fired is False:
        bulletSound = mixer.Sound("laser.wav")
        bulletSound.play()
    bullet.fire(player.possitionX, player.possitionY)
    bullet.possitionY -= bullet.speed
    draw_object(bullet.img, bullet.possitionX, bullet.possitionY)


def draw_game_titles():
    myfont = pygame.font.SysFont("Times", 33, "bold")
    label = myfont.render("Score: " + str(player.score), 1, (255, 255, 255))
    labelLive = myfont.render("Live: " + str(player.lives), 1, (138, 0, 0))
    screen.blit(label, (0, 0))
    screen.blit(labelLive, (0, 36))


def default_action():
    pass


def check_game_over():
    if player.lives == 0:
        return True
    else:
        return False


def check_win():
    if len(enemies) == 0:
        return True
    else:
        return False


def game_over():
    player.stop()

    game_over_label = bigFont.render("GAME OVER", 1, (255, 255, 255))
    restart_label = smallFont.render("Press F1 to resrt", 1, (255, 255, 255))

    screen.blit(game_over_label, (207, 240))
    screen.blit(restart_label, (0, 570))


def call_win():

    win_label = bigFont.render("You Win", 1, (255, 255, 255))
    restart_label = smallFont.render("Press F1 to restart", 1, (255, 255, 255))

    screen.blit(win_label, (270, 240))
    screen.blit(restart_label, (0, 570))


def restart():
    global player, enemies
    player = init_player()
    enemies = init_enemies(num_of_enemies)
    screen.fill((23, 12, 0))
    screen.blit(background, (0, 0))


def increase_key_action(x):
    return {
        pygame.K_RIGHT: player.move_right,
        pygame.K_LEFT: player.move_left,
        pygame.K_UP: player.move_up,
        pygame.K_DOWN: player.move_down,
        pygame.K_SPACE: fire_bullet,
        pygame.K_F1: restart,
    }.get(x, default_action)()


def game_menu():

    runningMenuLoop = True
    screen.blit(background, (0, 0))

    newGameBTN = pygame.image.load('newGamebtn.png').convert_alpha()
    newGameBTNX = 300
    newGameBTNY = 150
    newGameBTNRect = pygame.Rect((newGameBTNX, newGameBTNY), (200, 50))
    screen.blit(newGameBTN, (newGameBTNX, newGameBTNY))

    exitBTN = pygame.image.load('button_zakoncz.png').convert_alpha()
    exitBTNX = 300
    exitBTNY = 250
    exitBTNRect = pygame.Rect((exitBTNX, exitBTNY), (200, 50))
    screen.blit(exitBTN, (exitBTNX, exitBTNY))

    label = bigFont.render("SpaceEX Game", 1, (255, 255, 255))
    screen.blit(label, (180, 470))

    pygame.display.flip()

    while runningMenuLoop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if newGameBTNRect.collidepoint(event.pos):
                runningMenuLoop = False
            if exitBTNRect.collidepoint(event.pos):
                 exit()


def game_loop():
    global runningGameLoop
    runningGameLoop = True
    init_game()

    mixer.music.load("background.wav")
    mixer.music.play(-1)

    while runningGameLoop:

        screen.fill((23, 12, 0))
        screen.blit(background, (0, 0))

        move_enemies()

        player.updateMoves()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningGameLoop = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key is not None:
                    increase_key_action(key)
            if event.type == pygame.KEYUP:
                player.stop_moving(event.key)


        if bullet.fired:
            fire_bullet()

        draw_game_titles()
        draw_object(player.img, player.possitionX, player.possitionY)

        if check_game_over():
            game_over()

        if check_win():
            call_win()

        pygame.display.update()


if __name__ == "__main__":
    game_menu()
    game_loop()


