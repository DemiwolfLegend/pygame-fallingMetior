import pygame
import random
from pygame import mixer

pygame.init()

pygame.display.set_caption("firstGame")

screen = pygame.display.set_mode((800, 800))
backgroundImage = pygame.image.load("./content/background.png")
back_music = mixer.music.load("./content/background.wav")
mixer.music.play(-1)


class Bullet:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/bullet.png")
        self.x = 800
        self.y = 700
        self.change = 10
        self.state = False

    def aim(self, other):
        self.x = other.x
        self.y = other.y
        self.state = True

    def show(self):
        screen.blit(self.image, (self.x, self.y))
        # print(self.x, self.y)

    def move(self):
        self.y -= self.change
        if self.y < -10:
            self.state = False
            self.y = 700
            self.x = 800


class character:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/player.png")
        self.x = 350
        self.y = 700
        self.change = 0
        self.bullet = Bullet()

    def show(self):
        if self.bullet.state:
            self.bullet.move()
            self.bullet.show()
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.change
        if self.x < 0:
            self.x = 0
        elif self.x > 700:
            self.x = 700


class boulder:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/enemy.png")
        self.x = random.randint(0, 700)
        self.y = random.randint(-500, -100)
        self.change = 5
        self.num = 0

    def fall(self):
        self.y += self.change
        if self.y > 800:
            self.x = random.randint(0, 700)
            self.y = random.randint(-500, -100)

    def isColide(self, player):
        collison = self.y >= 600 and player.y > 0 and (
            self.x > (player.x-100) and self.x < (player.x+100))
        if collison:
            player.y = -600
            print("Game Over", self.num)
            self.num += 1
            return True
        else:
            return False

    def show(self):
        screen.blit(self.image, (self.x, self.y))


player = character()
enemy = []
numFall = 10
for i in range(numFall):
    enemy.append(boulder())

run = True
while run:
    screen.blit(backgroundImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change = -10
            elif event.key == pygame.K_RIGHT:
                player.change = 10
            elif event.key == pygame.K_SPACE:
                if not player.bullet.state:
                    player.bullet.aim(player)
        elif event.type == pygame.KEYUP:
            player.change = 0

    player.move()
    for i in range(numFall):
        enemy[i].fall()
        if enemy[i].isColide(player):
            break
        enemy[i].show()

    player.show()
    pygame.display.update()
